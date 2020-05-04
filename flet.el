(defun f () "old f")

(cl-letf (((symbol-function 'old-f) (lambda () (f)))
          ((symbol-function 'f)
           (lambda () (format "%s, %s" (old-f) "new f"))))
  (f))
;; => infinite recursion


(cl-flet ((old-f () (f)))
  (cl-letf (((symbol-function 'f)
             (lambda () (format "%s, %s" (old-f) "new f"))))
    (f)))
;; => infinite recursion


(cl-letf (((symbol-function 'old-f) #'f)
          ((symbol-function 'f)
           (lambda () (format "%s, %s" (old-f) "new f"))))
  (f))
;; => infinite recursion


(defun f () "old f")
(let ((f-fn (symbol-function 'f)))
  (cl-letf (((symbol-function 'f)
             (lambda () (format "%s, %s" (funcall f-fn) "new f"))))
    (f)))
