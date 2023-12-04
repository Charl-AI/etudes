import argparse
from collections import defaultdict
from enum import Enum
from typing import Literal, NamedTuple

from intcode import ProgramState, StopSignal, get_program, run_program


class Color(Enum):
    BLACK = 0
    WHITE = 1


class Turn(Enum):
    LEFT = 0
    RIGHT = 1


class Orientation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Position(NamedTuple):
    x: int
    y: int


def move_robot(
    position: Position, orientation: Orientation, turn: Turn
) -> tuple[Position, Orientation]:
    if turn == Turn.LEFT:
        orientation = Orientation((orientation.value - 1) % 4)
    elif turn == Turn.RIGHT:
        orientation = Orientation((orientation.value + 1) % 4)
    else:
        raise ValueError(f"Invalid turn: {turn}")

    if orientation == Orientation.UP:
        y = position.y + 1
        x = position.x
    elif orientation == Orientation.RIGHT:
        y = position.y
        x = position.x + 1
    elif orientation == Orientation.DOWN:
        y = position.y - 1
        x = position.x
    elif orientation == Orientation.LEFT:
        y = position.y
        x = position.x - 1
    else:
        raise ValueError(f"Invalid orientation: {orientation}")

    return Position(x, y), orientation


def run_robot(state: ProgramState):
    signal = StopSignal.WAITING
    position = Position(0, 0)
    orientation = Orientation.UP
    painted = {}

    inputs = [0]  # start on a black panel
    while signal != StopSignal.HALTED:
        signal, state, outputs = run_program(inputs, state)
        if len(outputs) != 2:
            raise ValueError("Expected two outputs from program.")

        color = Color(outputs[0])
        turn = Turn(outputs[1])

        painted[position] = color
        position, orientation = move_robot(position, orientation, turn)

        if position in painted:
            inputs = [painted[position].value]
        else:
            inputs = [0]  # unpainted panels are black

    return painted


def main(question: Literal["a", "b", "tests"], file_path: str):
    memory = get_program(file_path)

    if question == "a":
        state = ProgramState(memory, 0, 0)
        painted = run_robot(state)
        print(f"Part 1: {len(painted)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, default="a", help="Question part (a or b).")
    parser.add_argument("-f", type=str, default="input.txt", help="Path to input file")
    args = parser.parse_args()
    question = args.q
    filepath = args.f
    main(question, filepath)
