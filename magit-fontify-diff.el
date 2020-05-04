;; DNW

(defun magit-diff-syntax-fontify-hunk (section)
  (if (window-system)
      (let ((beg (magit-diff-hunk-region-beginning))
            (end (magit-diff-hunk-region-end)))
        (diff-syntax-fontify-hunk beg end nil))))

(setq magit-diff-highlight-hunk-region-functions (append magit-diff-highlight-hunk-region-functions '(magit-diff-syntax-fontify-hunk)))
