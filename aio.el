#!/usr/bin/env emacs --script
(setq-default lexical-binding t)
(setq lexical-binding t)
(add-to-list 'load-path "~/src/3p/emacs-aio")
(require 'aio)

(defun make-promise:call-function (seconds function)
  (let ((promise (aio-promise))
        (value-function (lambda () (assert lexical-binding) (funcall function))))
    (aio-listen promise (lambda (value-function) (funcall value-function)))
    (prog1 promise
      (run-at-time seconds nil #'aio-resolve promise value-function))))

(defun example-1 ()
  "Execute a function in the future."
  (message "starting example-1")
  (make-promise:call-function 1 (lambda () (message "example-1 callback"))))

(aio-defun example-2 ()
  "Execute two functions in the future."
  (aio-await (make-promise:call-function 3 (lambda () (message "example-2 callback 1"))))
  (aio-await (make-promise:call-function 1 (lambda () (message "example-2 callback 2")))))

(defun make-process-demo ()
  (make-process
   :name "example-3"
   :command '("bash-wrapper" "-c" "ls -l")
   :sentinel (lambda (process event) (message "example-3 callback"))))

(defun example-3 ()
  "Run a child process asynchronously."
  (let ((sentinel-file (format "/tmp/example-3-%s" (format-time-string "%s%3N%6N"))))
    (make-process-demo)))

(defun make-promise:make-process (callback)
  (let ((promise (aio-promise))
        (value-function callback))
    (aio-listen promise (lambda (value-function) (funcall value-function)))
    (prog1 promise
      (make-process
       :name "make-promise:make-process--process-name"
       :command '("/Users/dan/bin/bash-wrapper" "-c" "ls -l")
       :sentinel (lambda (process event) (message "sentinel") (aio-resolve promise value-function))))))

(aio-defun example-4 ()
  "Run a child processes asynchronously, using a promise"
  (make-promise:make-process (lambda () (message "example-4 callback 1"))))

(aio-defun example-5 ()
  "Run two child processes asynchronously, one after the other"
  (aio-await (make-promise:make-process (lambda () (message "example-5 callback 1"))))
  (aio-await (make-promise:make-process (lambda () (message "example-5 callback 2")))))

(defun run (fn)
  (with-current-buffer "*Messages*"
    (setq buffer-read-only nil)
    (goto-char (point-max))
    (insert "\n\n\n\n"))
  (funcall fn)
  (message "started %s" (symbol-name fn))
  (message ""))

(when (or noninteractive nil)
  (run 'example-3)
  )

(if noninteractive
    (sleep-for 5))
