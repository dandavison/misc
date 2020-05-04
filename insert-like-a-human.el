(defun dan/insert-like-a-human-0 (string)
  "Insert STRING as if typed interactively."
  ;; This isn't far off; the following renders when the command finishes
  ;; Inline $\dot{x}$ and
  (interactive "sText to insert: ")
  (let ((TeX-electric-math nil)
        (LaTeX-electric-left-right-brace nil))
    (mapc (lambda (c) (font-lock-fontify-buffer) (execute-kbd-macro `[,c]) (font-lock-fontify-buffer) (sit-for 0.05) (font-lock-fontify-buffer)) string)))


(defun dan/insert-like-a-human-1 (string)
  "Insert STRING as if typed interactively."
  (interactive "sText to insert: ")
  (let ((TeX-electric-math nil)
        (LaTeX-electric-left-right-brace nil))
    (mapc (lambda (c) (aio-with-async (execute-kbd-macro `[,c]) (sit-for 0.05) (font-lock-fontify-buffer))) string)))

(defun dan/insert-like-a-human-2 (string)
  "Insert STRING as if typed interactively."
  (interactive "sText to insert: ")
  (let ((TeX-electric-math nil)
        (LaTeX-electric-left-right-brace nil))
    (dolist (char (string-to-list string))
      (run-with-timer 0 nil (lambda () (execute-kbd-macro `[,char]) (sit-for 0.05))))))


(aio-defun dan/insert-like-a-human-3 (string)
  (interactive "sText to insert: ")
  (let ((TeX-electric-math nil)
        (LaTeX-electric-left-right-brace nil))
    (dolist (char (string-to-list string))
      (aio-await (aio-with-async (execute-kbd-macro `[,char]) (font-lock-fontify-buffer) (sit-for 0.05))))))

(aio-defun dan/insert-like-a-human (string)
  (interactive "sText to insert: ")
  (let ((TeX-electric-math nil)
        (LaTeX-electric-left-right-brace nil))
    (dolist (char (string-to-list string))
      (aio-await (aio-with-async (execute-kbd-macro `[,char])
                                 ;; (font-lock-fontify-buffer)
                                 ;; (redisplay)
                                 (cursor-sensor--detect (selected-window))
                                 (sit-for 0.05)
                                 (font-lock-fontify-buffer)
                                 (xenops-math-handle-element-transgression (selected-window) (1- (point)) 'left)
                                 ;; (redisplay)
                                 (cursor-sensor--detect (selected-window))
                                 (backward-char)
                                 (forward-char)
                                 (cursor-sensor--detect (selected-window))
                                 ;; (cursor-sensor--detect (selected-window))}
                                 ;; (font-lock-fontify-buffer)
                                 ;; (cursor-sensor--detect (selected-window))}
                                 ;; (redisplay)
                                 )))))

(defun dan/insert-like-a-human-fake (string)
  (interactive "sText to insert: ")
  (let ((TeX-electric-math nil)
        (LaTeX-electric-left-right-brace nil))
    (dolist (char (string-to-list string))
      (if (eq char ?`)
          (progn
            (xenops-math-handle-element-transgression (selected-window) (- (point) 2) 'left)
            (font-lock-fontify-buffer))
        (execute-kbd-macro `[,char])
        (sit-for 0.05)))))


(defun dan/insert-like-a-human (string)
  (interactive "sText to insert: ")
  (setq TeX-electric-math nil)
  (setq LaTeX-electric-left-right-brace nil)
  (setq unread-command-events (listify-key-sequence string)))
