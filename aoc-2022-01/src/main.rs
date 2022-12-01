use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let config = parse_config(&args);
    let contents =
        fs::read_to_string(config.file_path).expect("Something went wrong reading the file");

    if config.question == "a" {
        let result = solve_part_a(&contents);
        println!("The answer to part a is: {}", result);
    } else if config.question == "b" {
        let result = solve_part_b(&contents);
        println!("The answer to part b is: {}", result);
    } else {
        println!("Unknown question: {}", config.question);
    }
}

struct Config {
    question: String,
    file_path: String,
}

fn parse_config(args: &[String]) -> Config {
    // question is first arg, file path is second
    let question = &args[1];
    let file_path = &args[2];

    Config {
        file_path: file_path.to_string(),
        question: question.to_string(),
    }
}

// Very simple imperative solution. Loop through lines, keeping track of the current
// score and the best score seen so far.
fn solve_part_a(contents: &str) -> i32 {
    let mut best = 0;
    let mut current = 0;
    for line in contents.lines() {
        // empty lines delineate the different elves
        if line.is_empty() {
            if current > best {
                best = current;
            }
            current = 0;
        } else {
            current += line.parse::<i32>().unwrap();
        }
    }
    best
}

// Convert to list of summed scores, then sort and sum first 3.
fn solve_part_b(contents: &str) -> i32 {
    let mut scores: Vec<i32> = Vec::new();
    let mut current = 0;
    for line in contents.lines() {
        // empty lines delineate the different elves
        if line.is_empty() {
            scores.push(current);
            current = 0;
        } else {
            current += line.parse::<i32>().unwrap();
        }
    }
    scores.sort_unstable();
    let len = scores.len();
    scores[len - 1] + scores[len - 2] + scores[len - 3]
}
