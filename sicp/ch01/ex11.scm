; f:= {
; n if n<3,
; f(n-1) + 2f(n-2) + 3f(n-3) otherwise.
; }

; recursive implementation
(define (f n)
  (if (< n 3)
    n
    (+
      (f (- n 1))
      (* 2 (f (- n 2)))
      (* 3 (f (- n 3))))))

(f 1) ; -> 1
(f 2) ; -> 2
(f 4) ; -> 11
(f 8) ; -> 335
(f 16); -> 338870


; iterative/tail-recursive implementation
(define (g n)
  (define (inner nth n-1 n-2 n-3)
    (if (= n nth)
     n-1
     (inner (+ 1 nth)
            (+ n-1 (* 2 n-2) (* 3 n-3))
            n-1
            n-2)))

  (if (< n 3)
    n
    (inner 2 2 1 0)))


(g 1) ; -> 1
(g 2) ; -> 2
(g 4) ; -> 11
(g 8) ; -> 335
(g 16); -> 338870
