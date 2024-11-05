# Rust

We do the 2022 problems with the venerable rust!

## Running

We use cargo to build and run the code. Cargo is not really built for small scripts so we have to make a whole project directory for each challenge:

```bash
# create a cargo project for day 1
cargo new rust/day01

# enter project
cd rust/day01

# run project (no command line args needed)
cargo run
```

While we _could_ avoid the need to make these project directories by compiling and running with `rustc day01.rs -o /tmp/tmpbuild && /tmp/tmpbuild`, it is not ideal because most rust tooling (LSP etc.) assumes you are using cargo.
