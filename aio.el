#!/usr/bin/env emacs --script
(add-to-list 'load-path "~/src/3p/emacs-aio")
(setq-default lexical-binding t)
(setq lexical-binding t)
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

(defun example-3 ()
  "Run a child process asynchronously."
  (let ((sentinel-file (format "/tmp/example-3-%s" (format-time-string "%s%3N%6N"))))
    (make-process
     :name "example-3"
     :command '("bash-wrapper" "-c" "ls -l")
     :sentinel (lambda (process event) (message "example-3 callback")))))

(defun run (fn)
  (with-current-buffer "*Messages*"
    (setq buffer-read-only nil)
    (goto-char (point-max))
    (insert "\n\n\n\n"))
  (funcall fn)
  (message "started %s" (symbol-name fn))
  (message ""))

(when nil
  (run 'example-3)
  )
