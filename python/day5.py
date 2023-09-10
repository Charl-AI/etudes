import argparse
from enum import Enum
from typing import Literal


def get_inputs(file_path: str) -> list[int]:
    codes = []
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            for value in values:
                codes.append(int(value))
    return codes


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    END = 99


# Simply the number of parameters each opcode expects, including the opcode itself
OPCODE_LENGTHS = {
    Opcode.ADD: 4,
    Opcode.MULTIPLY: 4,
    Opcode.INPUT: 2,
    Opcode.OUTPUT: 2,
    Opcode.END: 1,
}


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def parse_instruction(instruction: int) -> tuple[Opcode, list[ParameterMode]]:
    """Parse an instruction into an opcode and a list of parameter modes."""
    instruction_str = str(instruction)
    opcode = Opcode(int(instruction_str[-2:]))
    modes = [ParameterMode(int(mode)) for mode in instruction_str[:-2]]

    # pad modes if necessary (padding with 0s is equivalent to POSITION mode)
    # list should have the same length as the number of parameters the opcode expects
    # i.e. OPCODE_LENGTHS[opcode] - 1
    if len(modes) < OPCODE_LENGTHS[opcode] - 1:
        modes = [ParameterMode.POSITION] * (
            OPCODE_LENGTHS[opcode] - len(modes) - 1
        ) + modes
    modes.reverse()  # reverse so that the first parameter is at index 0

    return opcode, modes


def process_params(
    codes: list[int], raw_params: list[int], modes: list[ParameterMode]
) -> list[int]:
    """Map raw parameters to their actual values based on their parameter modes."""
    return list(
        map(
            lambda x: x[0] if x[1] == ParameterMode.IMMEDIATE else codes[x[0]],
            zip(raw_params, modes),
        )
    )


def run_program(codes: list[int]) -> None:
    i = 0
    while True:
        opcode, modes = parse_instruction(codes[i])

        if opcode == Opcode.ADD:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[2] == ParameterMode.POSITION
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)
            codes[codes[i + 3]] = params[0] + params[1]

        elif opcode == Opcode.MULTIPLY:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[2] == ParameterMode.POSITION
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)
            codes[codes[i + 3]] = params[0] * params[1]

        elif opcode == Opcode.INPUT:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[0] == ParameterMode.POSITION
            codes[codes[i + 1]] = int(input("Enter input: "))

        elif opcode == Opcode.OUTPUT:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            param = process_params(codes, [codes[i + 1]], modes)
            print(param)

        elif opcode == Opcode.END:
            print("Opcode 99: END")
            break

        else:
            raise ValueError(f"Invalid opcode: {opcode}")

        i += OPCODE_LENGTHS[opcode]


def main(question: Literal["a", "b"], file_path: str):
    codes = get_inputs(file_path)

    if question == "a":
        run_program(codes)

    elif question == "b":
        pass

    else:
        raise ValueError(f"Invalid question: {question}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, default="a", help="Question part (a or b).")
    parser.add_argument("-f", type=str, default="input.txt", help="Path to input file")
    args = parser.parse_args()
    question = args.q
    filepath = args.f
    main(question, filepath)
