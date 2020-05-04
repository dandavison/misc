(defun product (&rest lists)
  (apply #'-table-flat (lambda (&rest args) args) lists))
