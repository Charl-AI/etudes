import argparse
from typing import Literal


def get_inputs(file_path: str) -> list[int]:
    codes = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            for value in values:
                codes.append(int(value))

    return codes


def run_program(codes: list[int]) -> list[int]:
    for i in range(0, len(codes), 4):
        opcode = codes[i]
        if opcode == 99:
            return codes
        elif opcode == 1:
            codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
        elif opcode == 2:
            codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    return codes


def brute_force_inputs(codes: list[int], target: int) -> int:
    codes2 = codes.copy()
    for i in range(100):
        for j in range(100):
            codes[1] = i
            codes[2] = j
            result = run_program(codes)
            if result[0] == target:
                return 100 * i + j
            codes = codes2.copy()

    raise ValueError("No solution found")


def main(question: Literal["a", "b"], file_path: str):
    codes = get_inputs(file_path)

    if question == "a":
        codes[1] = 12
        codes[2] = 2
        run_program(codes)
        print(codes[0])
        return

    if question == "b":
        print(brute_force_inputs(codes, 19690720))
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
