"""The intcode computer is complete at the end of day 9. This file contains the
completed computer for use in future days."""

from collections import defaultdict
from enum import Enum
from typing import NamedTuple


def get_program(file_path: str) -> dict[int, int]:
    """Program and memory share the same space (Von Neumann architecture).
    We represent the memory as a dict of addresses and values. Indicies outside
    of the program are implicitly initialized to 0."""
    memory = defaultdict(int)
    with open(file_path, "r") as file:
        for line in file:
            values = line.strip().split(",")
            for i, value in enumerate(values):
                memory[i] = int(value)
    return memory


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE_OFFSET = 9
    END = 99


# Simply the number of parameters each opcode expects, including the opcode itself
OPCODE_LENGTHS = {
    Opcode.ADD: 4,
    Opcode.MULTIPLY: 4,
    Opcode.INPUT: 2,
    Opcode.OUTPUT: 2,
    Opcode.JUMP_IF_TRUE: 3,
    Opcode.JUMP_IF_FALSE: 3,
    Opcode.LESS_THAN: 4,
    Opcode.EQUALS: 4,
    Opcode.RELATIVE_BASE_OFFSET: 2,
    Opcode.END: 1,
}

assert len(OPCODE_LENGTHS) == len(Opcode)


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


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


def get_params(
    memory: dict[int, int],
    opcode: Opcode,
    modes: list[ParameterMode],
    instruction: int,
    relative_base: int,
):
    """Fetch the parameters for the operation, given the opcode and modes."""

    raw_params = [memory[instruction + i] for i in range(1, OPCODE_LENGTHS[opcode])]

    def get_param_value(param: int, mode: ParameterMode) -> int:
        if mode == ParameterMode.POSITION:
            return memory[param]
        elif mode == ParameterMode.IMMEDIATE:
            return param
        elif mode == ParameterMode.RELATIVE:
            return memory[param + relative_base]
        else:
            raise ValueError(f"Invalid parameter mode: {mode}")

    params = [get_param_value(param, mode) for param, mode in zip(raw_params, modes)]
    assert len(params) == OPCODE_LENGTHS[opcode] - 1
    return params


class StopSignal(Enum):
    HALTED = 0
    WAITING = 1


class ProgramState(NamedTuple):
    """The state of the intcode program is a tuple of the current memory,
    the instruction index and the relative base offset."""

    memory: dict[int, int]
    instruction: int
    relative_base: int


def run_program(
    inputs: list[int], state: ProgramState
) -> tuple[StopSignal, ProgramState, list[int]]:
    """Run the intcode program. Stops when one of two conditions is met:
        1. The program halts (opcode 99)
        2. The program reaches an INPUT opcode after exhausting the inputs list

    Condition 1 results in a StopSignal of HALTED, while condition 2 results in a
    StopSignal of WAITING. Both conditions result in returning the outputs list,
    as well as the current program state and instruction index.

    Args:
        inputs (list[int]): Program inputs (one int is supplied at each INPUT opcode).
        state (ProgramState): State of the current program. Is a 3-tuple consisting of:
            memory (dict[int, int]): The intcode program.
            instruction (int): The current instruction index. Init this to.
            relative_base (int): The current relative base offset. Init this to 0.

    Returns:
        tuple[StopSignal, ProgramState, list[int]: A tuple containing the stop
        signal (HALTED or WAITING), the current state of the program, and the outputs.
    """
    memory, instruction, relative_base = state
    outputs = []
    i = instruction
    while True:
        opcode, modes = parse_instruction(memory[i])

        if opcode == Opcode.ADD:
            params = get_params(memory, opcode, modes, i, relative_base)
            output_address = (
                memory[i + 3]
                if modes[2] == ParameterMode.POSITION
                else (memory[i + 3] + relative_base)
            )
            memory[output_address] = params[0] + params[1]
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.MULTIPLY:
            params = get_params(memory, opcode, modes, i, relative_base)
            output_address = (
                memory[i + 3]
                if modes[2] == ParameterMode.POSITION
                else (memory[i + 3] + relative_base)
            )
            memory[output_address] = params[0] * params[1]
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.INPUT:
            params = get_params(memory, opcode, modes, i, relative_base)

            if len(inputs) == 0:
                current_state = ProgramState(memory, i, relative_base)
                return StopSignal.WAITING, current_state, outputs

            output_address = (
                memory[i + 1]
                if modes[0] == ParameterMode.POSITION
                else (memory[i + 1] + relative_base)
            )
            memory[output_address] = inputs.pop(0)
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.OUTPUT:
            params = get_params(memory, opcode, modes, i, relative_base)
            outputs.append(params[0])
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.JUMP_IF_TRUE:
            params = get_params(memory, opcode, modes, i, relative_base)

            if params[0] != 0:
                i = params[1]
            else:
                i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.JUMP_IF_FALSE:
            params = get_params(memory, opcode, modes, i, relative_base)

            if params[0] == 0:
                i = params[1]
            else:
                i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.LESS_THAN:
            # assert modes[2] == ParameterMode.POSITION
            params = get_params(memory, opcode, modes, i, relative_base)

            output_address = (
                memory[i + 3]
                if modes[2] == ParameterMode.POSITION
                else (memory[i + 3] + relative_base)
            )

            if params[0] < params[1]:
                memory[output_address] = 1
            else:
                memory[output_address] = 0

            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.EQUALS:
            params = get_params(memory, opcode, modes, i, relative_base)

            output_address = (
                memory[i + 3]
                if modes[2] == ParameterMode.POSITION
                else (memory[i + 3] + relative_base)
            )

            if params[0] == params[1]:
                memory[output_address] = 1
            else:
                memory[output_address] = 0

            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.RELATIVE_BASE_OFFSET:
            params = get_params(memory, opcode, modes, i, relative_base)
            relative_base += params[0]
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.END:
            current_state = ProgramState(memory, i, relative_base)
            return StopSignal.HALTED, current_state, outputs

        else:
            raise ValueError(f"Invalid opcode: {opcode}")
