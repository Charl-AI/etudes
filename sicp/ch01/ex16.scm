; consider this simple procedure for computing exponentials,
; where (expt b n) computes b^n.
(define (slow-expt b n)
  (if (= n 0)
    1
    (* b (expt b (- n 1)))))

(slow-expt 3 2) ; evaluates to 9
(slow-expt 2 3) ; evaluates to 8
(slow-expt 5 4) ; evaluates to 625

; the number of steps in the above process scales with O(n)
; we can reduce this to O(log n) by using the rule:
; b^n = {
;   b^(n/2)^2   if n is even,
;   b * b^(n-1) otherwise.
; }
(define (fast-expt b n)
  (define (square n)
    (* n n))
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(fast-expt 3 2) ; evaluates to 9
(fast-expt 2 3) ; evaluates to 8
(fast-expt 5 4) ; evaluates to 625

; finally, let's convert this into a tail-recursive procedure:
(define (super-fast-expt b n)
  (define (inner a b n)
    (cond ((= n 0) (a))
          ((even? n) (inner a (* b b) (/ n 2)))
          (else (inner (* a b) b (- n 1)))))
  (inner 1 b n))


(super-fast-expt 3 2) ; evaluates to 9
(super-fast-expt 2 3) ; evaluates to 8
(super-fast-expt 5 4) ; evaluates to 625
