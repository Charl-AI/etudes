use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let configs = Config::from_args(&args);
    let contents = configs.get_contents();

    match configs.question.as_str() {
        "a" => println!(
            "Answer to Part a: {}",
            get_score_for_tournament(&parse_contents_for_part_a(&contents))
        ),
        "b" => println!(
            "Answer to Part b: {}",
            get_score_for_tournament(&parse_contents_for_part_b(&contents))
        ),
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

#[derive(Eq, PartialEq, Clone)]
enum Action {
    Rock,
    Paper,
    Scissors,
}

impl Action {
    fn from_char(c: char) -> Action {
        match c {
            'A' => Action::Rock,
            'B' => Action::Paper,
            'C' => Action::Scissors,

            // these are only relevant in part a, where the letter represents our action
            'X' => Action::Rock,
            'Y' => Action::Paper,
            'Z' => Action::Scissors,
            _ => panic!("Invalid action"),
        }
    }

    fn score(&self) -> i32 {
        match self {
            Action::Rock => 1,
            Action::Paper => 2,
            Action::Scissors => 3,
        }
    }
}

#[derive(Eq, PartialEq)]
enum Result {
    Loss,
    Draw,
    Win,
}

impl Result {
    // only relevant in part a, where the result is calculated from the event
    fn from_event(event: &Event) -> Result {
        if event.our_action == event.their_action {
            Result::Draw
        } else if event.our_action == Action::Rock && event.their_action == Action::Scissors
            || event.our_action == Action::Paper && event.their_action == Action::Rock
            || event.our_action == Action::Scissors && event.their_action == Action::Paper
        {
            Result::Win
        } else {
            Result::Loss
        }
    }

    // only relevant in part b, where the result is given in the input
    fn from_char(c: char) -> Result {
        match c {
            'X' => Result::Loss,
            'Y' => Result::Draw,
            'Z' => Result::Win,
            _ => panic!("Invalid result"),
        }
    }

    fn score(&self) -> i32 {
        match self {
            Result::Loss => 0,
            Result::Draw => 3,
            Result::Win => 6,
        }
    }
}

struct Event {
    our_action: Action,
    their_action: Action,
}

impl Event {
    fn from_result_and_action(result: Result, their_action: Action) -> Event {
        if result == Result::Draw {
            Event {
                our_action: their_action.clone(),
                their_action,
            }
        } else if result == Result::Win {
            match their_action {
                Action::Rock => Event {
                    our_action: Action::Paper,
                    their_action,
                },
                Action::Paper => Event {
                    our_action: Action::Scissors,
                    their_action,
                },
                Action::Scissors => Event {
                    our_action: Action::Rock,
                    their_action,
                },
            }
        } else if result == Result::Loss {
            match their_action {
                Action::Rock => Event {
                    our_action: Action::Scissors,
                    their_action,
                },
                Action::Paper => Event {
                    our_action: Action::Rock,
                    their_action,
                },
                Action::Scissors => Event {
                    our_action: Action::Paper,
                    their_action,
                },
            }
        } else {
            panic!("Invalid result");
        }
    }

    fn score(&self) -> i32 {
        let action_score = self.our_action.score();
        let outcome_score = Result::from_event(self).score();
        action_score + outcome_score
    }
}

struct Tournament {
    events: Vec<Event>,
}

// In this puzzle, the computation is the same for both parts once we've got the events,
// the difference is how to parse the input into a tournament of events.

// in part a, the first letter is their action and the second is ours
fn parse_contents_for_part_a(contents: &str) -> Tournament {
    fn get_event_from_str(s: &str) -> Event {
        let mut chars = s.chars();
        let their_action = Action::from_char(chars.next().unwrap());
        let _ = chars.next(); // throw away the space between characters
        let our_action = Action::from_char(chars.next().unwrap());

        Event {
            our_action,
            their_action,
        }
    }
    let events = contents.lines().map(get_event_from_str).collect();
    Tournament { events }
}

// in part b, the first letter is their action and the second is the result
fn parse_contents_for_part_b(contents: &str) -> Tournament {
    fn get_event_from_str(s: &str) -> Event {
        let mut chars = s.chars();
        let their_action = Action::from_char(chars.next().unwrap());
        let _ = chars.next(); // throw away the space between characters
        let result = Result::from_char(chars.next().unwrap());

        Event::from_result_and_action(result, their_action)
    }
    let events = contents.lines().map(get_event_from_str).collect();
    Tournament { events }
}

fn get_score_for_tournament(tournament: &Tournament) -> i32 {
    tournament.events.iter().map(Event::score).sum()
}
