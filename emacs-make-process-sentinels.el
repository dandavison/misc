(defun my-sentinel (process event)
  (message "%s\n%s" (process-exit-status process) event))

(let ((command '("/usr/local/texlive/2018/bin/x86_64-darwin/latex" "-interaction" "nonstopmode" "-output-directory" "/var/folders/4y/_sf125x10zlgt4fw5vj2pk9h0000gn/T/" "/var/folders/4y/_sf125x10zlgt4fw5vj2pk9h0000gn/T/5d56429bee08780dbebb10f713e3ce966bb34024.tex")))
  (make-process
   :name "test-command"
   :command command
   :sentinel #'my-sentinel))

(let ((command '("latex" "-interaction" "nonstopmode" "/var/folders/4y/_sf125x10zlgt4fw5vj2pk9h0000gn/T/5d56429bee08780dbebb10f713e3ce966bb34024.tex")))
  (make-process
   :name "test-command"
   :command command
   :sentinel #'my-sentinel))

(call-process "/usr/local/texlive/2018/bin/x86_64-darwin/latex" nil nil nil "-interaction" "nonstopmode" "-output-directory" "/tmp/z" "/var/folders/4y/_sf125x10zlgt4fw5vj2pk9h0000gn/T/5d56429bee08780dbebb10f713e3ce966bb34024.tex")
