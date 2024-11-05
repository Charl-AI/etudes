import copy
from enum import Enum
from itertools import permutations
from typing import Literal

INPUT_FILE = "data/2019/day07.txt"


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
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
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


class StopSignal(Enum):
    HALTED = 0
    WAITING = 1


def run_program(
    codes: list[int], inputs: list[int], instruction: int = 0
) -> tuple[StopSignal, list[int], list[int], int]:
    """Run the intcode program. Stops when one of two conditions is met:
        1. The program halts (opcode 99)
        2. The program reaches an INPUT opcode after exhausting the inputs list

    Condition 1 results in a ProgramState of HALTED, while condition 2 results in a
    ProgramState of WAITING. Both conditions result in returning the outputs list,
    as well as the current program state and instruction index.

    Args:
        codes (list[int]): The intcode program.
        inputs (list[int]): Program inputs (one int is supplied at each INPUT opcode).
        instruction (int, optional): The current instruction index. Defaults to 0.

    Returns:
        tuple[ProgramState, list[int], list[int], int]: A tuple containing the program
        state (HALTED or WAITING), the outputs, the modified program, and the current
        instruction index.
    """
    outputs = []
    i = instruction
    while True:
        opcode, modes = parse_instruction(codes[i])

        if opcode == Opcode.ADD:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[2] == ParameterMode.POSITION
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)
            codes[codes[i + 3]] = params[0] + params[1]
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.MULTIPLY:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[2] == ParameterMode.POSITION
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)
            codes[codes[i + 3]] = params[0] * params[1]
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.INPUT:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[0] == ParameterMode.POSITION

            if len(inputs) == 0:
                return StopSignal.WAITING, outputs, codes, i
            codes[codes[i + 1]] = inputs.pop(0)
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.OUTPUT:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            param = process_params(codes, [codes[i + 1]], modes)
            outputs.append(param[0])
            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.JUMP_IF_TRUE:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)

            if params[0] != 0:
                i = params[1]
            else:
                i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.JUMP_IF_FALSE:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)

            if params[0] == 0:
                i = params[1]
            else:
                i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.LESS_THAN:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[2] == ParameterMode.POSITION
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)

            if params[0] < params[1]:
                codes[codes[i + 3]] = 1
            else:
                codes[codes[i + 3]] = 0

            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.EQUALS:
            assert len(modes) == OPCODE_LENGTHS[opcode] - 1
            assert modes[2] == ParameterMode.POSITION
            raw_params = codes[i + 1 : i + OPCODE_LENGTHS[opcode]]
            params = process_params(codes, raw_params, modes)

            if params[0] == params[1]:
                codes[codes[i + 3]] = 1
            else:
                codes[codes[i + 3]] = 0

            i += OPCODE_LENGTHS[opcode]

        elif opcode == Opcode.END:
            return StopSignal.HALTED, outputs, codes, i

        else:
            raise ValueError(f"Invalid opcode: {opcode}")


class Amplifier:
    def __init__(self, phase_setting: int, codes: list[int]) -> None:
        self.phase_setting = phase_setting
        self.codes = codes
        self.instruction = 0

        self._set_phase()

    def _set_phase(self) -> None:
        """Run first part of program to set the phase."""
        inputs = [self.phase_setting]
        stop_signal, outputs, codes, instruction = run_program(
            self.codes, inputs, self.instruction
        )
        self.codes = codes
        self.instruction = instruction

        # program should return a WAITING signal and no outputs
        assert stop_signal == StopSignal.WAITING
        assert len(outputs) == 0

    def process_signal(self, input_signal: int) -> tuple[StopSignal, list[int]]:
        """Run the program to process an input signal."""
        inputs = [input_signal]
        stop_signal, outputs, codes, instruction = run_program(
            self.codes, inputs, self.instruction
        )
        self.codes = codes
        self.instruction = instruction
        return stop_signal, outputs


def run_amplifier_chain(codes: list[int], phase_settings: list[int]) -> int:
    amps = [Amplifier(setting, copy.deepcopy(codes)) for setting in phase_settings]
    output = 0

    for amp in amps:
        stop_signal, outputs = amp.process_signal(output)
        assert stop_signal == StopSignal.HALTED
        assert len(outputs) == 1
        output = outputs[0]
    return output


def run_amplifier_loop(codes: list[int], phase_settings: list[int]) -> int:
    amps = [Amplifier(setting, copy.deepcopy(codes)) for setting in phase_settings]
    output = 0

    while True:
        for idx, amp in enumerate(amps):
            stop_signal, outputs = amp.process_signal(output)
            assert len(outputs) == 1
            output = outputs[0]

            if stop_signal == StopSignal.HALTED and idx == 4:
                return output


def main(file_path: str):
    codes = get_inputs(file_path)

    max_output = 0
    for phase_settings in list(permutations(range(5))):
        output = run_amplifier_chain(codes, phase_settings)  # type: ignore
        if output > max_output:
            max_output = output
    print("Solution to part a:")
    print(f"Max output: {max_output}")

    max_output = 0
    for phase_settings in list(permutations(range(5, 10))):
        output = run_amplifier_loop(codes, phase_settings)  # type: ignore
        if output > max_output:
            max_output = output
    print("Solution to part b:")
    print(f"Max output: {max_output}")


if __name__ == "__main__":
    main(INPUT_FILE)
