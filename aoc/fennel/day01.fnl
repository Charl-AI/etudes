(fn lines-from-file [filepath]
  (let [fin (io.open filepath "r")]
    (icollect [line (fin:lines)] line)))


(local input (lines-from-file "data/2020/day1.txt"))

(each [_ num (ipairs input)]
 (print num))

(fn in [tbl key]
  "Check if a table contains a key."
  (if (= nil (?. tbl key))
      false
      true))



(let [tbl {:key1 1 :key2 2}]
  ; print tbl)
  (in tbl :key1))

(let [ans {}]
    (tset ans 1341 true)
    (let [inside (in ans 1341)]
      print inside))

; (print (. nums-required 1933))
; (when (. nums-required 1933)
    ;    (print "hi"))
; (let [num-completes-sum? (. nums-required num)]
    ; (print num-completes-sum?)
; this is the classic TwoSum problem,
; returns the two elements in the
; nums table that sum to the target
(fn two-sum [nums target]
  (let [nums-required {} ans []]
    (each [_ num (ipairs nums)]
      (if (. nums-required num)
        (do
          (tset ans 1 num)
          (tset ans 2 (- target num)))
        (tset nums-required (- target num) true)))
    ans))

(fn two-sum [nums target]
  (let [nums-required {} ans []]
    (each [_ num (ipairs nums)]
      (tset nums-required (- target num) true))

    (each [_ num (ipairs nums)]
      (let [num-completes-sum? (. nums-required num)]
        (when num-completes-sum?
          (tset ans 1 num)
          (tset ans 2 (- target num)))))

    ans))



                ; (set ans.1 idx)
; (set ans.2 (. tbl num)))
(two-sum input 2020)

(. (two-sum input 2020) 2005)



(let [test {}]
  (for [i 1 10])


  print (. test 12))
