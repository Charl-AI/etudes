use std::fs;

static INPUT_FILE: &str = "../../data/2022/day01.txt";

fn main() {
    let contents = fs::read_to_string(INPUT_FILE).expect("The file path should be valid");
    let inputs = parse_contents(&contents);

    println!("Answer to Part a: {}", solve_part_a(&inputs));
    println!("Answer to Part b: {}", solve_part_b(&inputs));
}

struct Troupe {
    elves: Vec<Elf>,
}

struct Elf {
    inventory: Vec<i32>,
}

impl Elf {
    fn total_carried(&self) -> i32 {
        self.inventory.iter().sum()
    }
}

// Construct a Troupe of Elves from the string contents of the input file
// imperative implementation -- perhaps it's more idiomatic to use fold/map?
fn parse_contents(contents: &str) -> Troupe {
    let mut elf = Elf {
        inventory: Vec::new(),
    };
    let mut troupe = Troupe { elves: Vec::new() };
    for line in contents.lines() {
        if line.is_empty() {
            // empty lines separate elves
            troupe.elves.push(elf);
            elf = Elf {
                inventory: Vec::new(),
            };
        } else {
            let item = line.parse::<i32>().unwrap();
            elf.inventory.push(item);
        }
    }
    troupe
}

fn solve_part_a(troupe: &Troupe) -> i32 {
    troupe.elves.iter().map(Elf::total_carried).max().unwrap()
}

fn solve_part_b(troupe: &Troupe) -> i32 {
    let mut scores: Vec<i32> = troupe.elves.iter().map(Elf::total_carried).collect();

    // I'm a bit confused as to why I had to do this. All I know is that the compiler wouldn't let
    // me do it the obvious way, i.e. scores.sort().reverse().iter().take(3).sum()
    {
        scores.sort();
        scores.reverse();
    }
    scores.iter().take(3).sum()
}
