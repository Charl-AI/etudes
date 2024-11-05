use std::fs;

static INPUT_FILE: &str = "../../data/2022/day07.txt";
fn main() {
    let contents = fs::read_to_string(INPUT_FILE).expect("The file path should be valid");
    let files = Files::from_contents(&contents);

    println!("Answer to Part a: {}", solve_part_a(&files));
    println!("Answer to Part b: {}", solve_part_b(&files));
}

struct Files {
    sizes: std::collections::HashMap<String, usize>,
}

impl Files {
    fn from_contents(contents: &str) -> Files {
        let mut filepath = Vec::new();
        let mut sizes = std::collections::HashMap::new();
        for line in contents.lines() {
            if line.starts_with('$') {
                match line {
                    "$ cd /" => filepath.push("/"),
                    "$ ls" => {} // no need to worry about ls
                    "$ cd .." => {
                        filepath.pop().unwrap();
                    }
                    // this is the general case of 'cd <dir>'
                    _ => {
                        let dir = line.split_whitespace().last().unwrap();
                        filepath.push(dir);
                    }
                }
            } else {
                let filesize = line.split_whitespace().next().unwrap().parse::<usize>();

                if let Ok(fs) = filesize {
                    let mut dir = String::new();
                    for p in filepath.iter() {
                        dir.push('/');
                        dir.push_str(p);
                        dir = dir.replace("//", "/");
                        *sizes.entry(dir.clone()).or_insert(0) += fs;
                    }
                }
            }
        }
        Files { sizes }
    }

    fn total_sizes_below_threshold(&self, threshold: usize) -> usize {
        let mut total = 0;
        for (_, size) in self.sizes.iter() {
            if *size < threshold {
                total += size;
            }
        }
        total
    }

    fn smallest_dir_above_threshold(&self, threshold: usize) -> usize {
        self.sizes
            .iter()
            .filter(|(_, size)| **size > threshold)
            .collect::<Vec<_>>()
            .iter()
            .map(|(_, size)| **size)
            .min()
            .unwrap()
    }
}

fn solve_part_a(files: &Files) -> usize {
    files.total_sizes_below_threshold(100000)
}

fn solve_part_b(files: &Files) -> usize {
    let current_size = files.sizes.get("/").unwrap();
    let threshold = current_size + 30000000 - 70000000;
    files.smallest_dir_above_threshold(threshold)
}
