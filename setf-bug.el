(defun f ()
  (list 'orig))

(defun g ()
  (let ((val (f)))
    (message "before: %S" val)
    (setf (nth 0 val) 'new)
    (message "after: %S" val)
    nil))
