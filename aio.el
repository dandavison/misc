#!/usr/bin/env emacs --script
;; -*- lexical-binding: t -*-
(add-to-list 'load-path "~/src/3p/emacs-aio")
(require 'aio)

(defun print-closure (closure)
  (dolist (n '(0 1 2 3 4))
    (message "%d: %S" n (nth n closure))))

(defun make-promise:schedule-function (seconds function)
  (let ((promise (aio-promise))
        (value-function (lambda () (cl-assert lexical-binding) (funcall function))))
    (aio-listen promise (lambda (fn)
                          (message "closure:\n")
                          (print-closure fn)
                          (funcall fn)))
    (prog1 promise
      (run-at-time seconds nil #'aio-resolve promise value-function))))

(defun example-1 ()
  "Execute a function in the future."
  (message "starting example-1")
  (make-promise:schedule-function 1 (lambda () (message "example-1 callback"))))

(aio-defun example-2 ()
  "Execute two functions in the future."
  (aio-await (make-promise:schedule-function 3 (lambda () (message "example-2 callback 1"))))
  (aio-await (make-promise:schedule-function 1 (lambda () (message "example-2 callback 2")))))

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
    (aio-listen promise (lambda (value-function) (funcall value-function)))
    (let ((sentinel (lambda (process event)
                      (message "make-promise:start-process-with-sentinel: sentinel callback")
                      (cl-assert lexical-binding)
                      (cl-assert (boundp 'promise))
                      (aio-resolve promise value-function))))
      (prog1 promise
        (make-process-demo sentinel)))))

(defun example-4 ()
  "Run a child processes asynchronously, using a promise"
  (make-promise:start-process-with-sentinel (lambda () (message "example-4 callback 1"))))

(aio-defun example-5 ()
  "Run two child processes asynchronously, one after the other"
  (aio-await (make-promise:start-process-with-sentinel (lambda () (message "example-5 callback 1"))))
  (aio-await (make-promise:start-process-with-sentinel (lambda () (message "example-5 callback 2")))))

(defun run (fn)
  (with-current-buffer "*Messages*"
    (setq buffer-read-only nil)
    (goto-char (point-max))
    (insert "\n\n\n\n"))
  (funcall fn)
  (message "started %s" (symbol-name fn))
  (message ""))

(when noninteractive
  (run 'example-1)
  (dolist (_ '(0 0 0 0 0 0 0 0))
    (sleep-for 1)))


