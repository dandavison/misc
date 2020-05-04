;; short-circuiting version of dash -find-index
(defun -find-index (pred list)
  (catch :index
    (let ((i 0))
      (dolist (el list)
        (and (funcall pred el) (throw :index i))
        (setq i (1+ i))))))
