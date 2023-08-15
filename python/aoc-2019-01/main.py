import argparse
from typing import Literal


def get_inputs(file_path):
    masses = []
    with open(file_path, "r") as file:
        for line in file:
            mass = int(line.strip())
            masses.append(mass)
    return masses


def main(question: Literal["a", "b"], file_path: str):
    masses = get_inputs(file_path)

    if question == "a":
        print(sum(map(lambda mass: mass // 3 - 2, masses)))
        return

    if question == "b":
        raise NotImplementedError

    raise ValueError(f"Invalid question: {question}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, default="a", help="Question part (a or b).")
    parser.add_argument("-f", type=str, default="input.txt", help="Path to input file")
    args = parser.parse_args()
    question = args.q
    filepath = args.f
    main(question, filepath)
