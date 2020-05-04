(xenops-apply 'regenerate
              (lambda (el) (string-match "\\Im" (buffer-substring (plist-get el :begin)
                                                             (plist-get el :end)))))
