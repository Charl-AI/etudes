use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let configs = Config::from_args(&args);
    let contents = configs.get_contents();

    let inputs = parse_contents(&contents);

    match configs.question.as_str() {
        "a" => println!("Answer to Part a: {}", solve_part_a(&inputs)),
        "b" => println!("Answer to Part b: {}", solve_part_b(&inputs)),
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
