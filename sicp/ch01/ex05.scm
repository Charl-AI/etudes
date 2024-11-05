; applicative-order application (which scheme uses)
; involves evaluating the arguments to a function first,
; the substituting. This contrasts to normal-order application,
; where you substitute then expand, then reduce.

; Essentially: applicative=eager, normal=lazy

; this procedure evaluates to 0 using normal order because
; the interpreter never tries to evaluate (p).
; In applicative order, it will recurse forever or return an error

(define (p) (p))

(define (test x y)
  if (= x 0) 0 y)

(test 0 (p))
