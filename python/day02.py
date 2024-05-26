import copy

INPUT_FILE = "data/2019/day02.txt"


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


def main(file_path: str):
    codes = get_inputs(file_path)

    part_a_codes = copy.deepcopy(codes)
    part_a_codes[1] = 12
    part_a_codes[2] = 2
    run_program(part_a_codes)
    print("Solution to part a:")
    print(part_a_codes[0])

    part_b_codes = copy.deepcopy(codes)
    print("Solution to part b:")
    print(brute_force_inputs(part_b_codes, 19690720))


if __name__ == "__main__":
    main(INPUT_FILE)
