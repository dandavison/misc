(defun magit-translate-ansi-colors-in-region--ansi-color--text-properties (beg end)
  (error "text properties will not work")
  (let ((ansi-color-apply-face-function
         (lambda (beg end face)
           (put-text-property beg end 'font-lock-face face))))
    (ansi-color-apply-on-region beg end)))


(defun magit-translate-ansi-colors-in-region--xterm-color--text-properties (beg end)
  (error "text properties will not work")
  (require 'xterm-color)
  (save-restriction
    (narrow-to-region beg end)
    (let ((inhibit-read-only t)
          (buffer-read-only nil))
      (xterm-color-colorize-buffer))))



(flet ((show (bytes) (--map (format "%0x" it) bytes)))
  (message "%s -> %s" (show bytes) (show crc)))

(defun png-set-phys-integer-to-bytes (int)
  ())

(dolist (indices (list x-ppm-indices
                       y-ppm-indices))
  (cl-loop for (index byte) in (-zip indices ppm-bytes) do
           (aset png (1- index) byte)))
(--map (s-join "" it) (-partition 2 (s-split "" (format "%08x" 960) t)))
(format "%08x" 960)
"000003c0"



