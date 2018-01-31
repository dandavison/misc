(defun filter (pred lst)
  (when lst
       (if (funcall pred (car lst))
           (cons (car lst) (filter pred (cdr lst)))
         (filter pred (cdr lst)))))

(filter (lambda (x) (< x 5)) '(1 2 3 4))
