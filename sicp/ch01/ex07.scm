; bad procedure for finding square root

(define (average x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (average guess (/ x guess)))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
    guess
    (sqrt-iter (improve guess x) x)))


; evaluates to 3.00009155... (approximately correct)
(sqrt-iter 1.0 9)


; evaluates to 0.0412... (actual answer is 0.0316...)
; this is incorrect because the good-enough? procedure has
; a hardcoded tolerance that does not work well for small numbers
(sqrt-iter 1.0 0.001)


; gets stuck on some large numbers because good-enough? cannot
; be satisfied to within floating point error
(sqrt-iter 1.0 1e21)


; improved good-enough? function returns true when the change between
; the current-guess and prev-guess is less than 0.1% of the current-guess
(define (good-enough2? current-guess prev-guess)
  (< (/ (abs (- current-guess prev-guess)) current-guess) 0.0001))

(define (sqrt-iter2 guess x)
  (let ((better (improve guess x)))
    (if (good-enough2? better guess)
     guess
     (sqrt-iter2 (improve guess x) x))))


; evaluates to 3.00009155...
(sqrt-iter2 1.0 9)

; evaluates to 0.031622...
(sqrt-iter2 1.0 0.001)

; evaluates to 31622778383 (approximately correct)
(sqrt-iter2 1.0 1e21)
