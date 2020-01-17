#!/usr/bin/env emacs --script
;; -*- lexical-binding: t -*-
(add-to-list 'load-path "~/src/3p/emacs-aio")
(require 'aio)

(defun task (n)
  (message "starting task %s" n)
  (sleep-for 1)
  (message "finished task %s" n))

(dolist (n '(1 2 3 4 5 6 7 8))
  (task n))
