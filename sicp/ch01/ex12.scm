; Pascal's triangle:
;    1
;   1 1
;  1 2 1
; 1 3 3 1
;
; Let's use 1-based indexing, i.e.
; row 1, col 1 = 1
; row 2, col 2 = 1
; row 3, col 2 = 2
; row 4, col 3 = 3

; Thus:
; P(row, col) = {
;  1 if col = 1 or col = row,
;  P(row-1, col-1) + P(row-1, col) otherwise.
; }

(define (P row col)
  (cond ((= col 1) 1)
        ((= col row) 1)
        (else (+
                (P (- row 1) (- col 1))
                (P (- row 1) col)))))

(P 1 1)
(P 2 2)
(P 3 2)
(P 4 3)


(define (display-pascal-row n)
  (define (column-iter i)
    (display (P n i)) (display "  ")
    (if (= i n)
        (newline)
        (column-iter (+ i 1))))
  (column-iter 1))

(define (display-pascal n)
  (define (display-pascal-iter i)
    (display-pascal-row i)
    (if (= i n)
        (newline)
        (display-pascal-iter (+ i 1))))
  (display-pascal-iter 1))

(display-pascal 10)
