; the following does not work because new-if evaluates
; both of its arguments, so the recursive call will get stuck
; and will never hit the base case

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x) x)))
