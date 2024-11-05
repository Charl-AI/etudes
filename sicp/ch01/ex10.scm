; Ackerman's function
(define (A x y)
  (cond ((= y 0) 0)
    ((= x 0) (* 2 y))
    ((= y 1) 2)
    (else (A (- x 1) (A x (- y 1))))))

; evaluates to 1024
(A 1 10)

; evaluates to 65536
(A 2 4)

; evaluates to 65536
(A 3 3)

; computes 2n
(define (f n) (A 0 n))

; computes 2^n
(define (g n) (A 1 n))

; computes 2^(2^2...) where the 'stack of powers' is n high
(define (h n) (A 2 n))
