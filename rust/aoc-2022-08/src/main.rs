use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let configs = Config::from_args(&args);
    let contents = configs.get_contents();

    let forest = Forest::new(&contents);

    match configs.question.as_str() {
        "a" => println!("Answer to Part a: {}", solve_part_a(forest)),
        "b" => println!("Answer to Part b: {}", solve_part_b(forest)),
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

struct Forest {
    trees: Vec<Vec<u32>>,
}

impl Forest {
    fn new(contents: &str) -> Forest {
        let mut trees = Vec::new();
        for line in contents.lines() {
            trees.push(line.chars().map(|c| c.to_digit(10).unwrap()).collect());
        }
        Forest { trees }
    }

    // a tree is visible from a direction if every tree outside it has a smaller value
    // the code is a bit messy because the trees are in a grid so we check all 4 directions
    fn visible_trees(&self) -> Vec<Vec<u32>> {
        let mut visible_trees = vec![vec![0; self.trees[0].len()]; self.trees.len()];

        for row in 0..self.trees.len() {
            visible_trees[row][0] = 1;
            let mut largest_seen = self.trees[row][0];
            for col in 1..self.trees[0].len() {
                if self.trees[row][col] > largest_seen {
                    largest_seen = self.trees[row][col];
                    visible_trees[row][col] = 1;
                }
            }
        }

        for col in 0..self.trees[0].len() {
            visible_trees[0][col] = 1;
            let mut largest_seen = self.trees[0][col];
            for row in 1..self.trees.len() {
                if self.trees[row][col] > largest_seen {
                    largest_seen = self.trees[row][col];
                    visible_trees[row][col] = 1;
                }
            }
        }

        for row in (0..self.trees.len()).rev() {
            visible_trees[row][self.trees.len() - 1] = 1;
            let mut largest_seen = self.trees[row][self.trees.len() - 1];
            for col in (0..self.trees[0].len() - 1).rev() {
                if self.trees[row][col] > largest_seen {
                    largest_seen = self.trees[row][col];
                    visible_trees[row][col] = 1;
                }
            }
        }

        for col in (0..self.trees[0].len()).rev() {
            visible_trees[self.trees.len() - 1][col] = 1;
            let mut largest_seen = self.trees[self.trees.len() - 1][col];
            for row in (0..self.trees.len() - 1).rev() {
                if self.trees[row][col] > largest_seen {
                    largest_seen = self.trees[row][col];
                    visible_trees[row][col] = 1;
                }
            }
        }

        visible_trees
    }

    fn scenic_score(&self) -> Vec<Vec<u32>> {
        let mut scenic_score = vec![vec![0; self.trees[0].len()]; self.trees.len()];

        for row in 1..self.trees.len() - 1 {
            for col in 1..self.trees[0].len() - 1 {
                // score from a direction is the number of trees before finding a larger tree
                let tree_size = self.trees[row][col];

                let left_score = self.trees[row][0..col]
                    .iter()
                    .rev()
                    .take_while(|&t| t < &tree_size)
                    .count() as u32;

                let right_score = self.trees[row][col + 1..]
                    .iter()
                    .take_while(|&t| t < &tree_size)
                    .count() as u32;

                let transposed_trees = transpose(self.trees.clone());

                let up_score = transposed_trees[col][0..row]
                    .iter()
                    .rev()
                    .take_while(|&t| t < &tree_size)
                    .count() as u32;

                let down_score = transposed_trees[col][row + 1..]
                    .iter()
                    .take_while(|&t| t < &tree_size)
                    .count() as u32;

                scenic_score[row][col] = left_score * right_score * up_score * down_score;
            }
        }

        scenic_score
    }
}

fn transpose<T>(original: Vec<Vec<T>>) -> Vec<Vec<T>> {
    assert!(!original.is_empty());
    let mut transposed = (0..original[0].len()).map(|_| vec![]).collect::<Vec<_>>();

    for original_row in original {
        for (item, transposed_row) in original_row.into_iter().zip(&mut transposed) {
            transposed_row.push(item);
        }
    }

    transposed
}

fn solve_part_a(forest: Forest) -> u32 {
    let visible_trees = forest.visible_trees();
    visible_trees.iter().flatten().sum()
}

fn solve_part_b(forest: Forest) -> u32 {
    let scenic_score = forest.scenic_score();
    *scenic_score.iter().flatten().max().unwrap()
}
