; найти какой день был под данной датой
(defun whatDay(day month year)
    (setq a (// (- 14 month) 12))
    (setq y (- year a))
    (setq m (- (+ (* 12 a) month) 2))

    (setq ab (// (* 31 m) 12))
    (setq bc (- (// y 4) (// y 100)))
    (setq xy (+ day y bc (// y 400) ab))
    (setq result (- (% (+ 7000 xy) 7) 1))

    (setq result (reculc result))

    (if (= result (- 0 1)) "sunday")
    (if (= result 0) "monday")
    (if (= result 1) "tuesday")
    (if (= result 2) "wednesday")
    (if (= result 3) "thursday")
    (if (= result 4) "friday")
    (if (= result 5) "saturday")
    (if (= result 6) "sunday" result)
)

(defun delneg(n)
    (if (< n 0) (- 0 n) n)
)

(defun ifneg(n)
    (if (< n 0) 1 0)
)

(defun reculc(result)
    (if (= isneg 1) (- result 1) result)
)

(readint n)

(setq isneg (ifneg n))
(setq n (delneg n))

(setq curyear (% n 10000))
(setq n (// n 10000))
(setq curmonth (% n 100))
(setq n (// n 100))
(setq curday (% n 100))
(setq n (// n 100))

; (print curyear)
; (print curmonth)
; (print curday)

(print "")
(write "Day: ")
(print (whatDay curday curmonth curyear))