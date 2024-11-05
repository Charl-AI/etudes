use std::fs;

static INPUT_FILE: &str = "../../data/2022/day06.txt";

fn main() {
    let contents = fs::read_to_string(INPUT_FILE).expect("The file path should be valid");
    let signal = Signal::new(&contents);

    println!("Answer to Part a: {}", solve_part_a(&signal));
    println!("Answer to Part b: {}", solve_part_b(&signal));
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
    fn first_unique_window(&self, window_length: usize) -> usize {
        let mut window_start = 0;
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
    signal.first_unique_window(4)
}

fn solve_part_b(signal: &Signal) -> usize {
    signal.first_unique_window(14)
}
