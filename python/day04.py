PUZZLE_INPUT = "183564-657474"


def monotonic_digits(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    return all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1))


def contains_double_digit(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    return any(digits[i] == digits[i + 1] for i in range(len(digits) - 1))


def no_triple_digits(number: int) -> bool:
    """This condition is a bit trickier. Complexes of three or more digits
    are disallowed, unless there is a separate double digit somewhere else in
    the number e.g. 111122 is valid, but 111222 is not."""

    digits = [int(d) for d in str(number)]
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            if i == 0:
                if digits[i + 1] != digits[i + 2]:
                    return True
            elif i == len(digits) - 2:
                if digits[i - 1] != digits[i]:
                    return True
            else:
                if digits[i - 1] != digits[i] and digits[i + 1] != digits[i + 2]:
                    return True
    return False


def solve_part_a():
    range_start, range_end = [int(n) for n in PUZZLE_INPUT.split("-")]
    candidate_numbers = range(range_start, range_end + 1)

    monotonic_numbers = filter(monotonic_digits, candidate_numbers)
    monotonic_and_doubles = filter(contains_double_digit, monotonic_numbers)

    return len(list(monotonic_and_doubles))


def solve_part_b():
    range_start, range_end = [int(n) for n in PUZZLE_INPUT.split("-")]
    candidate_numbers = range(range_start, range_end + 1)

    monotonic_numbers = filter(monotonic_digits, candidate_numbers)
    monotonic_and_doubles = filter(contains_double_digit, monotonic_numbers)
    monotonic_doubles_no_triples = filter(no_triple_digits, monotonic_and_doubles)

    return len(list(monotonic_doubles_no_triples))


def main():
    print("Solution to part a:")
    print(solve_part_a())

    print("Solution to part b:")
    print(solve_part_b())


if __name__ == "__main__":
    main()
