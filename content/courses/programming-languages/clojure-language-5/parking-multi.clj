(defmulti parking (fn [person num-months] (:type person)))

; faculty parking rate is $2000/year
(defmethod parking :faculty
  [person num-months]
  (* num-months (/ 2000.0 12)))

; student parking rate is $40/month
(defmethod parking :student
  [person num-months]
  (* num-months 40.0))

; no other types are supported
(defmethod parking :default
  [person num-months]
  nil)

; ============================
; test the code
; ============================

(let [einstein {:type :faculty
                :name "Albert Einstein"}
      jack {:type :student
            :name "Jack"}]
  (doseq [person [einstein jack]]
    (printf "%s pays $%.2f for 5 months of parking.\n" 
            (:name person)
            (parking person 5))))
