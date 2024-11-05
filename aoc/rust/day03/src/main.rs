use std::fs;

static INPUT_FILE: &str = "../../data/2022/day03.txt";

fn main() {
    let contents = fs::read_to_string(INPUT_FILE).expect("The file path should be valid");
    let supplies = Supplies::from_file_contents(&contents);

    println!("Answer to Part a: {}", solve_part_a(&supplies));
    println!("Answer to Part b: {}", solve_part_b(&supplies));
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

#[derive(Debug, Clone)]
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

impl Supplies {
    fn from_file_contents(contents: &str) -> Supplies {
        let rucksacks = contents
            .lines()
            .map(|l| Rucksack {
                items: l.to_string(),
            })
            .collect();

        Supplies { rucksacks }
    }
}

// in part b, the supplies are grouped into chunks of 3. This is a vector of the groups
// (which are represented as fixed size arrays)
struct GroupedSupplies {
    groups: Vec<[Rucksack; 3]>,
}

impl GroupedSupplies {
    fn from_supplies(supplies: &Supplies) -> GroupedSupplies {
        GroupedSupplies {
            groups: supplies
                .rucksacks
                .chunks(3)
                .map(|chunk| [chunk[0].clone(), chunk[1].clone(), chunk[2].clone()])
                .collect(),
        }
    }

    fn get_common_item(group: &[Rucksack; 3]) -> char {
        let (rucksack_0, rucksack_1, rucksack_2) = (&group[0], &group[1], &group[2]);
        let mut seen_in_0 = std::collections::HashSet::new();
        let mut seen_in_0_and_1 = std::collections::HashSet::new();

        for c in rucksack_0.items.chars() {
            seen_in_0.insert(c);
        }
        for c in rucksack_1.items.chars() {
            if seen_in_0.contains(&c) {
                seen_in_0_and_1.insert(c);
            }
        }
        for c in rucksack_2.items.chars() {
            if seen_in_0_and_1.contains(&c) {
                return c;
            }
        }
        panic!("No common item found");
    }
}

fn solve_part_a(supplies: &Supplies) -> i32 {
    supplies
        .rucksacks
        .iter()
        .map(Rucksack::get_duplicate_item)
        .map(Alphabet::get_character_score)
        .sum()
}

fn solve_part_b(supplies: &Supplies) -> i32 {
    let grouped_supplies = GroupedSupplies::from_supplies(supplies);
    grouped_supplies
        .groups
        .iter()
        .map(GroupedSupplies::get_common_item)
        .map(Alphabet::get_character_score)
        .sum()
}
