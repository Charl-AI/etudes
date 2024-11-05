; evaluates to 10
10

; evaluates to 12
(+ 5 3 4)

; evaluates to 3
(/ 6 2)

; evaluates to 6
(+ (* 2 4) (- 4 6))


(define a 3)
(define b (+ a 1))

; evaluates to 4
b

; evaluates to 19
(+ a b (* a b))

; evaluates to False
(= a b)

; evaluates to 4
(if (and (> b a) (< b (* a b)))
  b
  a)

; evaluates to 16
(cond ((= a 4) 6)
      ((= b 4) (+ 6 7 a))
      (else 25))

; evaluates to 6
(+ 2 (if (> b a) b a))

; evaluates to 16
(* (cond (( > a b) a)
         ((< a b) b)
         (else -1))
   (+ a 1))
