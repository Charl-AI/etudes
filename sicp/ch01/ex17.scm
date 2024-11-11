; If we pretend that our language does not support multiplication,
; we can design the following O(n) multiplication procedure:
(define (mult a b)
  (if (= b 0)
    0
    (+ a (mult a (- b 1)))))

(mult 5 4) ; 20
(mult 6 6) ; 36
(mult 2 0) ; 0

(define (double x)
  (* x 2))

(define (half x)
  (/ x 2))

; Like in ex 16, we can reduce this to O(log n) by using the rule:
; a * b = {
; a * double(half(b)) if b is even,
; a + a * (b - 1) otherwise.
; }
; assuming the lanuage comes with half/double functions
(define (fast-mult a b)
  (cond ((= b 0) 0)
        ((= b 1) a)
        ((even? b) (fast-mult a (double (half b))))
        (else (+ a (fast-mult a (- b 1))))))

(fast-mult 5 4) ; 20
(fast-mult 6 6) ; 36
(fast-mult 2 0) ; 0
