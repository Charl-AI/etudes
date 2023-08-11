# (Common) Lisp

Lisp is an old language, often credited as the first to include conditionals, recursion, first-class functions, garbage collection, and more. It has a slightly odd syntax, relying on 'S-expressions' with lots of parentheses. The key thing that makes this syntax so powerful is that it does not need to be parsed into an abstract syntax tree. The language _is_ already an AST.

Lisp is generally developed with active use of a REPL. We will use sbcl (with rlwrap to make the REPL a bit nicer). Start the REPL with `rlwrap sbcl`.
