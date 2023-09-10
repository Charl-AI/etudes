import argparse
from typing import Literal


def get_inputs(file_path: str):
    masses = []
    with open(file_path, "r") as file:
        for line in file:
            mass = int(line.strip())
            masses.append(mass)
    return masses


def get_fuel_recursive(mass: int):
    if mass <= 0:
        return 0
    fuel_mass = max(mass // 3 - 2, 0)
    return fuel_mass + get_fuel_recursive(fuel_mass)


def main(question: Literal["a", "b"], file_path: str):
    masses = get_inputs(file_path)

    if question == "a":
        print(sum(map(lambda mass: mass // 3 - 2, masses)))
        return

    if question == "b":
        print(sum(map(get_fuel_recursive, masses)))
        return

    raise ValueError(f"Invalid question: {question}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, default="a", help="Question part (a or b).")
    parser.add_argument("-f", type=str, default="input.txt", help="Path to input file")
    args = parser.parse_args()
    question = args.q
    filepath = args.f
    main(question, filepath)
