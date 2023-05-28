# Lua

We solve the 2021 problems in lua. We use lua 5.4.6. Note that this is slightly different to the version neovim uses (5.1).

## Basics

We implement scripts with the same interface to solve all problems. Run these scripts with `lua main.lua a input.txt` (change a to b for part b).

Lua is a very simple language. It has one data structure, [tables](https://www.lua.org/pil/11.3.html), and 8 [types](https://www.lua.org/pil/2.html). Most data structures may be implemented through tables. Also note that the `number` type uses double precision floats to represent *all* numbers.

