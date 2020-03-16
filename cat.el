#!/usr/bin/env emacs --script
(let ((package-load-list '((dash t) (s t) (f t)))) (package-initialize))
(require 'f)
(f-write-bytes (apply #'unibyte-string (append (f-read-bytes "/dev/stdin") nil)) "/dev/stdout")
