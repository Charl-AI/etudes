use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let configs = Config::from_args(&args);
    let contents = configs.get_contents();

    let signal = Signal::new(&contents);

    match configs.question.as_str() {
        "a" => println!("Answer to Part a: {}", solve_part_a(&signal)),
        "b" => println!("Answer to Part b: {}", solve_part_b(&signal)),
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

struct Signal {
    contents: Vec<char>,
}

impl Signal {
    fn new(contents: &str) -> Signal {
        Signal {
            contents: contents.chars().collect(),
        }
    }

    // returns true if every character in the window is unique
    fn is_window_unique(&self, window_start: usize, window_length: usize) -> bool {
        let mut seen = std::collections::HashSet::new();
        for i in window_start..window_start + window_length {
            if seen.contains(&self.contents[i]) {
                return false;
            }
            seen.insert(self.contents[i]);
        }
        true
    }

    // returns the index of the end of the first unique window, not the start
    fn first_unique_window(&self) -> usize {
        let mut window_start = 0;
        let window_length = 4;
        while window_start + window_length < self.contents.len() {
            if self.is_window_unique(window_start, window_length) {
                return window_start + window_length;
            }
            window_start += 1;
        }
        panic!("No unique window found");
    }
}

fn solve_part_a(signal: &Signal) -> usize {
    signal.first_unique_window()
}

fn solve_part_b(signal: &Signal) -> usize {
    unimplemented!()
}
