(defprotocol IPayee
  (parking [x months])
  (tuition [x credits]))

(defrecord Faculty [name]
  IPayee
  (parking [x months]
    (if (= name "Albert Einstein")
      0
      (* months (/ 2000.0 12))))
  (tuition [x credits]
    (if (= name "Richard Feynman")
      0
      (* credits 1.0))))

(defrecord Student [name]
  IPayee
  (parking [x months] (* 40.0 months))
  (tuition [x credits] (* 100.0 credits)))

(defn report [x months credits]
    (printf "%s taking %d credits in %d months costs %.2f\n"
            (:name x) months credits
            (+ (parking x months) (tuition x months))))


;; ========= testing ============

(let [p1 (Faculty. "Albert Einstein")
      p2 (Faculty. "Richard Feynman")
      p3 (Student. "Jack")]
  (report p1 4 40)
  (report p2 4 40)
  (report p3 4 40))
