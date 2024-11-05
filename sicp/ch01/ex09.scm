; both procedures implement summation of two numbers
; by adding one to the value of b and subtracting 1
; from the value of a. This process is repeated until
; the value of a reaches 0 (dec and inc are functions
; that - or + 1, respectively).

; this prodedure is recursive:
; (+ 3 4)
; (inc (+ 2 4))
; (inc (inc (+ 1 4)))
; (inc (inc (inc (+ 0 4))))
; (inc (inc (inc 4)))
; (inc (inc 5))
; (inc 6)
; 7
(define (+ a b)
  (if (= a 0) b (inc (+ (dec a) b))))


; this procedure is tail-recursive, so becomes iterative
; due to tail call optimisation by the compiler:
; (+ 3 4)
; (+ 2 5)
; (+ 1 6)
; (+ 0 7)
; 7
(define (+ a b)
  (if (= a 0) b (+ (dec a) (inc b))))
