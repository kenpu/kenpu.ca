(defprotocol IPayee
  (parking [x months])
  (tuition [x credits]))

(deftype Faculty [name]
  IPayee
  (parking [x months]
    (if (= name "Albert Einstein")
      0
      (* months (/ 2000.0 12))))
  (tuition [x credits]
    (if (= name "Richard Feynman")
      0
      (* credits 1.0))))

(deftype Student [name]
  IPayee
  (parking [x months] (* 40.0 months))
  (tuition [x credits] (* 100.0 credits)))

(defn report [x name months credits]
    (printf "%s taking %d credits in %d months costs %.2f\n"
            name months credits
            (+ (parking x months) (tuition x months))))


;; ========= testing ============

(let [p1 (Faculty. "Albert Einstein")
      p2 (Faculty. "Richard Feynman")
      p3 (Student. "Jack")]
  (report p1 "Albert" 4 40)
  (report p2 "Richard" 4 40)
  (report p3 "Jack" 4 40))
