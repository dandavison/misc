(defn get-methods [obj]
  (set
   (map (fn [m] (.getName m))
        (-> obj
            .getClass
            .getMethods))))

(defn print-methods [obj]
  (dorun (map println (sort (get-methods obj)))))
