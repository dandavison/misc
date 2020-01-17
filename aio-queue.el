#!/usr/bin/env emacs --script
;; -*- lexical-binding: t -*-
(add-to-list 'load-path "~/src/3p/emacs-aio")
(require 'aio)

(defun runif ()
  (/ (random 100) 100.0))

(aio-defun task (n)
  (message "starting %s" n)
  (aio-await (aio-sleep (runif)))
  (message "checkpoint %s" n)
  (message "finished %s" n))

(setq all-tasks-promise
      (aio-all (mapcar #'task '(1 2 3 4 5 6 7 8))))

(dolist (n (number-sequence 1 20))
  (message "main %s" n)
  (sleep-for 0.1))

(aio-wait-for all-tasks-promise)
