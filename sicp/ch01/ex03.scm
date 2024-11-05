; procedure to take three numbers and return the sum
; of the squares of the two largest numbers

(define (max2-sum-square a b c)
  (cond ((and (<= a b) (<= a c)
          (+ (* b b) (* c c))))
        ((and (<= b a) (<= b c)
          (+ (* a a) (* c c))))
        ((and (<= c a) (<= c b)
          (+ (* a a) (* b b))))))

(max2-sum-square 1 2 3)
