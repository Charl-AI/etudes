; Newton's formula for cubed roots:
; y = cuberoot(x), where
; y_n = (x / y^2 + 2y) / 3

(define (improve guess x)
  (/ (+ (/ x (* guess guess)) (* 2 guess)) 3))


(define (good-enough? current-guess prev-guess)
  (< (/ (abs (- current-guess prev-guess)) current-guess) 0.0001))

(define (cuberoot-iter guess x)
  (let ((better (improve guess x)))
   (if (good-enough? better guess)
    guess
    (cuberoot-iter (improve guess x) x))))


; evaluates to 2.0000049...
(cuberoot-iter 1.0 8)

; evaluates to 6.3467...
(cuberoot-iter 1.0 256)
