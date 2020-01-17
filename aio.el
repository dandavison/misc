#!/usr/bin/env emacs --script
;; -*- lexical-binding: t -*-
(add-to-list 'load-path "~/src/3p/emacs-aio")
(require 'aio)

;; aio is a library for management of asynchronous tasks. "Asynchronous" means that once the task
;; is started, the thread moves on to do something else. Callbacks can be registered such that they
;; are called in the future, when the task is completed or fails.

;; In addition, it's possible to write code that looks like normal synchronous code, but which is
;; in fact asynchronous. This uses `aio-defun' and `aio-await' and looks like
;;
(when nil

  (first-conventional-code-line)
  (start-async-tasks)
  (second-conventional-code-line)

  (aio-defun start-async-tasks ()
    (aio-await (start-first-task-and-return-promise))
    (start-second-task)))

;; Here, the second task will only be started when the first is finished. However, the thread is
;; not blocked in between. Instead it moves on to execute the next line of conventional code, but
;; when the first task finishes, and the thread is idle and available for a context switch,
;; start-second-task will be run.
;;
;; For comparison, in conventional callback-based code, this would look something like:

(when nil

  (first-conventional-code-line)
  (start-first-task-and-do-callback-when-finished
   (lambda () (start-second-task)))
  (second-conventional-code-line))

;; Functions like `start-first-task-and-return-promise` return an object known as a promise. A
;; promise object contains two things:
;;
;; 1. The callbacks that have been registered to be called when the task is finished.
;;
;; 2. When the task is finished ("resolved"), a function describing the result of the task is
;;    stored in the promise object.

;; A typical sequence of events in the lifecycle of a promise is:
;;
;; 1. Create promise: (setq promise (aio-promise)).
;; 2. Register listener callbacks: (aio-listen promise callback-taking-one-arg:the-value-function).
;; 3. The thread moves on to do something else.
;; 4. Something resolves the promise: (aio-resolve promise value-function-determined-by-resolver).
;; 5. The listener callbacks are called.
;;
;; To resolve a promise means to:
;;
;; 1. Construct a "value function". This is a function of no arguments that does/returns something.
;;    It often has "success" or "failure" semantics.
;;
;; 2. Make a pass through the listener callbacks that have been registered: for each one, call it,
;;    passing it the value function.
;;

;; Here is an example of a function that starts a task, and returns a promise.
(defun make-promise:schedule-function (seconds function)
  "Schedule FUNCTION to be called SECONDS seconds in the future. Return the associated promise."
  (let ((promise (aio-promise))
        (value-function (lambda ()
                          (funcall function))))
    (prog1 promise
      (run-at-time seconds nil #'aio-resolve promise value-function))))

;; Note that the value function isn't actually called at resolve time; it is just passed to
;; listeners. There are two ways to cause a promise's value function to be called:
;;
;; (1) Register a listener callback that calls the value function that it receives.
;; (2) Pass the promise to `aio-await`.
;;
;; `example-1' demonstrates (1).
;; `example-2' demonstrates (2).

(defun example-1 ()
  "Execute a function in the future. A listener is registered
that calls the value function."
  (let ((promise (make-promise:schedule-function 1 (lambda () (message "example-1 callback")))))
    (aio-listen promise (lambda (value-function)
                          (funcall value-function)))))

(aio-defun example-2 ()
  "Execute two functions in the future. No listeners are
registered, but we use `aio-await' which calls the value
function."
  (aio-await (make-promise:schedule-function 3 (lambda ()
                                                 (message "example-2 callback 1 %s" (format-time-string "%s%3N%6N")))))
  (aio-await (make-promise:schedule-function 1 (lambda ()
                                                 (message "example-2 callback 2 %s" (format-time-string "%s%3N%6N"))))))

(defun make-process-demo (sentinel)
  (make-process
   :name "demo-process-name"
   :command '("bash-wrapper" "-c" "ls -l")
   :sentinel sentinel))

;; (sentinel-file (format "/tmp/example-3-%s" (format-time-string "%s%3N%6N")))

(defun example-3 ()
  "Run a child process asynchronously."
  (make-process-demo
   (lambda (process event) (message "example-3 sentinel callback"))))

(defun make-promise:start-process-with-sentinel (callback)
  (let ((promise (aio-promise))
        (value-function callback))
    (let ((sentinel (lambda (process event)
                      (message "make-promise:start-process-with-sentinel: sentinel callback")
                      (aio-resolve promise value-function))))
      (prog1 promise
        (make-process-demo sentinel)))))

(defun example-4 ()
  "Run a child processes asynchronously, using a promise. A
listener is registered that calls the value function."
  (let ((promise (make-promise:start-process-with-sentinel (lambda ()
                                                             (message "example-4 callback")))))
    (aio-listen promise #'funcall)))

(aio-defun example-5 ()
  "Run two child processes asynchronously, one after the other"
  (aio-await (make-promise:start-process-with-sentinel (lambda () (message "example-5 callback 1"))))
  (aio-await (make-promise:start-process-with-sentinel (lambda () (message "example-5 callback 2")))))

(defun run (fn)
  (with-current-buffer "*Messages*"
    (setq buffer-read-only nil)
    (goto-char (point-max))
    (insert "\n\n\n\n"))
  (let ((name (symbol-name fn)))
    (message "starting %s" name)
    (funcall fn)
    (message "started %s" name)
    (message "")))

(defun print-closure (closure)
  (message "closure:\n")
  (dolist (n '(0 1 2 3 4))
    (message "%d: %S" n (nth n closure))))

(when noninteractive
  (run 'example-1)
  (run 'example-2)
  (run 'example-3)
  (run 'example-4)
  (run 'example-5)
  (dolist (_ '(0 0 0 0 0 0))
    (sleep-for 1)))


