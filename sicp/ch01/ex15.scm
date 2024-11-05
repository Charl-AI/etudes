; Computing sin x (radians) with the following procedure:
; sin x = {
;   x if x < 0.1,
;   3sin(x/3) - 4 sin^3(x/3) otherwise.
;   }
; iteration stops when x/3^n < 0.1, where x is initial value
; and n is number of steps. Thus number of iterations is
; O(log x)

(define (cube x) (* x x x))
(define (p x) (- (* 3 x) (* 4 (cube x))))
(define (sine ang step)
  (display step) (newline)
  (if (not (> (abs ang) 0.1))
    ang
    (p (sine (/ ang 3.0) (+ 1 step)))))


(sine 0.1 1)   ; evaluates to 0.10, takes 1 step
(sine 0.5 1)   ; evaluates to 0.48, takes 3 steps
(sine 1.0 1)   ; evaluates to 0.84, takes 4 steps
(sine 2.0 1)   ; evaluates to 0.91, takes 4 steps
(sine 4.0 1)   ; evaluates to -0.8, takes 5 steps
(sine 12.15 1) ; evaluates to -0.4, takes 6 steps
(sine 16.0 1)  ; evaluates to -0.3, takes 6 steps
(sine 32 1)    ; evaluates to 0.55, takes 7 steps
(sine 128 1)   ; evaluates to 0.66, takes 8 steps
