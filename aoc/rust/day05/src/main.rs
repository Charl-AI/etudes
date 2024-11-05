use std::fs;

// NB the use of words such as 'cargo' and 'crate' in this file are related to the question,
// not the Rust tooling

static INPUT_FILE: &str = "../../data/2022/day05.txt";

fn main() {
    let contents = fs::read_to_string(INPUT_FILE).expect("The file path should be valid");
    let mut cargo_a = Cargo::from_contents(&contents);
    let mut cargo_b = Cargo::from_contents(&contents);

    println!("Answer to Part a: {}", solve_part_a(&mut cargo_a));
    println!("Answer to Part b: {}", solve_part_b(&mut cargo_b));
}

struct Crate {
    contents: char,
}

impl Crate {
    // unpack expects string in form "A", or " ". If whitespace, returns None
    fn unpack(contents: char) -> Option<Crate> {
        if contents.is_whitespace() {
            return None;
        }
        // necessary but not sufficient checks, should be fine given our input file
        assert!(contents.is_alphabetic());
        assert!(contents.is_uppercase());
        Some(Crate { contents })
    }
}

struct CrateStack {
    crates: Vec<Crate>,
}

impl CrateStack {
    fn pop(&mut self) -> Option<Crate> {
        self.crates.pop()
    }
    fn push(&mut self, crate_: Crate) {
        self.crates.push(crate_)
    }
    fn is_empty(&self) -> bool {
        self.crates.is_empty()
    }
    fn peek(&self) -> Option<&Crate> {
        self.crates.last()
    }
}

struct Cargo {
    stacks: Vec<CrateStack>,
    // we include the file contents because it contains the move instructions
    contents: String,
}

impl Cargo {
    fn from_contents(contents: &str) -> Cargo {
        let mut stacks: Vec<CrateStack> = Vec::new();
        // populate with empty stacks
        for _ in 0..9 {
            stacks.push(CrateStack { crates: Vec::new() });
        }

        for line in contents.lines().take(8) {
            for (i, c) in line.chars().enumerate() {
                // letters are at line indices 1,5,9,13 ...
                if i % 4 == 1 {
                    if let Some(crate_) = Crate::unpack(c) {
                        stacks[(i - 1) / 4].push(crate_)
                    }
                }
            }
        }
        // order must be reversed because we built the stack top to bottom
        for stack in stacks.iter_mut() {
            stack.crates.reverse();
        }

        Cargo {
            stacks,
            contents: contents.to_string(),
        }
    }

    // instruction is string of form "move 3 from 9 to 4"
    // cratemover 9000 moves one crate at a time
    fn cratemover_9000_move_from_instruction(&mut self, instruction: &str) {
        let mut words = instruction.split_whitespace();
        // note: .nth() consumes the iterator, so we repeat .nth(1) to get 1,3,5
        let num = words.nth(1).unwrap().parse::<usize>().unwrap();
        let from_stack = words.nth(1).unwrap().parse::<usize>().unwrap();
        let to_stack = words.nth(1).unwrap().parse::<usize>().unwrap();

        for _ in 0..num {
            let crate_ = self.stacks[from_stack - 1].pop().unwrap();
            self.stacks[to_stack - 1].push(crate_);
        }
    }

    // instruction is string of form "move 3 from 9 to 4"
    // cratemover 9001 moves multiple crates at a time
    fn cratemover_9001_move_from_instruction(&mut self, instruction: &str) {
        let mut words = instruction.split_whitespace();
        // note: .nth() consumes the iterator, so we repeat .nth(1) to get 1,3,5
        let num = words.nth(1).unwrap().parse::<usize>().unwrap();
        let from_stack = words.nth(1).unwrap().parse::<usize>().unwrap();
        let to_stack = words.nth(1).unwrap().parse::<usize>().unwrap();

        let mut moving_crates = Vec::new();
        for _ in 0..num {
            moving_crates.push(self.stacks[from_stack - 1].pop().unwrap());
        }

        for _ in 0..num {
            self.stacks[to_stack - 1].push(moving_crates.pop().unwrap());
        }
    }

    fn get_top_layer(&self) -> String {
        let mut top_layer = String::new();
        for stack in self.stacks.iter() {
            if stack.is_empty() {
                top_layer.push(' ');
            } else {
                top_layer.push(stack.peek().unwrap().contents);
            }
        }
        top_layer
    }
}

fn solve_part_a(cargo: &mut Cargo) -> String {
    let contents = cargo.contents.clone();
    let instructions = contents.lines().skip(10);

    for instruction in instructions {
        Cargo::cratemover_9000_move_from_instruction(cargo, instruction);
    }
    cargo.get_top_layer()
}

fn solve_part_b(cargo: &mut Cargo) -> String {
    let contents = cargo.contents.clone();
    let instructions = contents.lines().skip(10);

    for instruction in instructions {
        Cargo::cratemover_9001_move_from_instruction(cargo, instruction);
    }
    cargo.get_top_layer()
}
