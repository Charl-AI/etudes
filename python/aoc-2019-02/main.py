import argparse
from typing import Literal


def get_inputs(file_path: str):
    codes = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            for value in values:
                codes.append(int(value))

    return codes


def run_program(codes):
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


def main(question: Literal["a", "b"], file_path: str):
    codes = get_inputs(file_path)

    if question == "a":
        codes[1] = 12
        codes[2] = 2
        run_program(codes)
        print(codes[0])
        return

    if question == "b":
        pass

    raise ValueError(f"Invalid question: {question}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, default="a", help="Question part (a or b).")
    parser.add_argument("-f", type=str, default="input.txt", help="Path to input file")
    args = parser.parse_args()
    question = args.q
    filepath = args.f
    main(question, filepath)
