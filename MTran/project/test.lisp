; однострочный комментарий
{ многострочный комментарий }

(print (/= 5 3))
; True
(print (= 5 (+ 2 3)))
; True
(print (= 10 (+ 2 3)))
; False
(print "")

(defun weird-function(n)
    (setq n 4)
    (print n)
)

(setq n 98)
(setq abc 17)
(weird-function abc)
; 4
(print abc)
; 17

(setq var 100)                  ; var = 100
(setq a (+ 111 222))            ; a = 123 + 456 => 579
(print a)
(setq a (+ 4 6 8) b 123456)   ; a = 6, b = 123456

(write "var = ")(print var)   ; printing var
(write "a = ")(print a)
(write "b = ")(print b)

(defun factorial(n acc)
  (if (= n 0) acc)
  (factorial (- n 1) (* n acc))
)

(write "factorial 13 = ")(print (factorial 13 1))        ; factorial 20

{ Fibonacci number }
(defun fibonacci(n)
	(fibonacci-iter 0 1 n)
)

(defun fibonacci-iter(a b n)
	(if (= n 0) 0)
	(if (= n 1) 1)

	(setq result (+ a b))
	(fibonacci-iter b result (- n 1))
)

(setq n 112)
(fibonacci n)
(write "fibonacci 112 = ")(print result)
