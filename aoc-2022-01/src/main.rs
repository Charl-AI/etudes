use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let config = parse_config(&args);
    let contents =
        fs::read_to_string(config.file_path).expect("Something went wrong reading the file");
    println!("With text:\n{contents}");

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

fn solve_part_a(contents: &String) -> i32 {
    0
}

fn solve_part_b(contents: &String) -> i32 {
    0
}
