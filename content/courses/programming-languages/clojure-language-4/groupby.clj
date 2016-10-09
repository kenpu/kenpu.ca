(defn inc-or-1 [n] (if (nil? n) 1 (inc n)))

(defn count-seq0 [xs]
  (if (empty? xs)
    {}
    (let [head (first xs)
          tail (rest xs)]
      (update (count-seq0 tail) head inc-or-1))))

(defn count-seq [xs cnt]
  (if (empty? xs)
    cnt
    (let [head (first xs)
          tail (rest xs)]
      (recur tail (update cnt head inc-or-1))))) 

(defn -main []
  (let [N 1000001]
    (try 
      (println (count-seq0 (repeat N :a)))
      (catch Throwable e (println "count-seq0 failed")))
    (try (println (count-seq (repeat N :a) {})))))

(-main)

