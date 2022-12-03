use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let configs = Config::from_args(&args);
    let contents = configs.get_contents();

    let inputs = parse_contents(&contents);

    match configs.question.as_str() {
        "a" => println!("Answer to Part a: {}", solve_part_a(&inputs)),
        "b" => println!("Answer to Part b: {}", unimplemented!()),
        _ => println!("Question must be a or b, got {}", configs.question),
    }
}

struct Config {
    question: String,
    file_path: String,
}

impl Config {
    fn from_args(args: &[String]) -> Config {
        let question = args[1].clone();
        let file_path = args[2].clone();
        Config {
            question,
            file_path,
        }
    }

    fn get_contents(&self) -> String {
        fs::read_to_string(&self.file_path).expect("The file path should be valid")
    }
}

enum Alphabet {}

impl Alphabet {
    fn get_character_score(c: char) -> i32 {
        let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        alphabet
            .find(c)
            .expect("The character should be in the alphabet") as i32
            + 1
    }
}

#[derive(Debug)]
struct Rucksack {
    items: String,
}

impl Rucksack {
    // Split into two compartments and find the common item between them
    // O(n+m), create hashmap for compartment 1, then check against compartment 2
    fn get_duplicate_item(&self) -> char {
        let midpoint = self.items.chars().count() / 2;
        let (comp1, comp2) = self.items.split_at(midpoint);

        let mut seen = std::collections::HashSet::new();
        for c in comp1.chars() {
            seen.insert(c);
        }
        for c in comp2.chars() {
            if seen.contains(&c) {
                return c;
            }
        }
        panic!("No duplicate item found");
    }
}

struct Supplies {
    rucksacks: Vec<Rucksack>,
}

fn parse_contents(contents: &str) -> Supplies {
    let mut supplies = Supplies {
        rucksacks: Vec::new(),
    };
    for line in contents.lines() {
        supplies.rucksacks.push(Rucksack {
            items: line.to_string(),
        });
    }
    supplies
}

fn solve_part_a(supplies: &Supplies) -> i32 {
    supplies
        .rucksacks
        .iter()
        .map(Rucksack::get_duplicate_item)
        .map(Alphabet::get_character_score)
        .sum()
}
