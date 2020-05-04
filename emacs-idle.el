#!/usr/bin/env emacs --script

(progn
  (run-with-idle-timer 0 nil (lambda () (message "in callback")))
  (sleep-for 2)
  (message "after sleep"))
