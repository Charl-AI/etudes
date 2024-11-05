INPUT_FILE = "data/2019/day01.txt"


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


def main(file_path: str):
    masses = get_inputs(file_path)

    print("Solution to part a:")
    print(sum(map(lambda mass: mass // 3 - 2, masses)))

    print("Solution to part b:")
    print(sum(map(get_fuel_recursive, masses)))


if __name__ == "__main__":
    main(INPUT_FILE)
