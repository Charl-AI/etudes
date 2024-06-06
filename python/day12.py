import math
from typing import NamedTuple

INPUT_FILE = "data/2019/day12.txt"


class Z3VectorSpace(NamedTuple):
    """3D integer vector space."""

    x: int
    y: int
    z: int

    def add(self, other: tuple[int, int, int]):
        assert len(other) == 3
        return Z3VectorSpace(self.x + other[0], self.y + other[1], self.z + other[2])

    def scale(self, scalar: int):
        assert isinstance(scalar, int)
        return Z3VectorSpace(self.x * scalar, self.y * scalar, self.z * scalar)

    def l1_norm(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)


Velocity = Z3VectorSpace
Position = Z3VectorSpace


class Moon(NamedTuple):
    position: Position
    velocity: Velocity

    def energy(self) -> int:
        return self.position.l1_norm() * self.velocity.l1_norm()


def apply_gravity(moons: list[Moon]) -> list[Moon]:
    updated_moons = []
    for moon1 in moons:
        velocity = moon1.velocity
        for moon2 in moons:
            if moon1 is moon2:
                continue

            p1 = moon1.position
            p2 = moon2.position
            dp = p2.add(p1.scale(-1))  # p2 - p1

            dv = tuple(
                map(lambda pos: 0 if pos == 0 else int(math.copysign(1, pos)), dp)
            )  # change in vel is 0 if same pos, else +-1, depending on the sign of the difference
            assert len(dv) == 3
            velocity = velocity.add(dv)

        updated_moons.append(Moon(moon1.position, velocity))
    return updated_moons


def apply_velocity(moons: list[Moon]) -> list[Moon]:
    updated_moons = []
    for moon in moons:
        new_position = moon.position.add(moon.velocity)
        updated_moons.append(Moon(new_position, moon.velocity))
    return updated_moons


def energy_t1k(moons: list[Moon]) -> int:
    for _ in range(1000):
        moons = apply_gravity(moons)
        moons = apply_velocity(moons)
    total_energy = sum(moon.energy() for moon in moons)
    return total_energy


def get_cycle_len(moons: list[Moon]) -> int:
    # each axis is independent, so we can find the cycle length of each and take the lcm
    # we will hit a cycle for an axis if the positions and velocities of all moons on that
    # axis are the same as the starting conditions.
    def get_state(moons):
        return (
            [(moon.position.x, moon.velocity.x) for moon in moons],
            [(moon.position.y, moon.velocity.y) for moon in moons],
            [(moon.position.z, moon.velocity.z) for moon in moons],
        )

    initial_state = get_state(moons)
    cycle_lengths = [0, 0, 0]

    iterations = 1
    while not (cycle_lengths[0] and cycle_lengths[1] and cycle_lengths[2]):
        moons = apply_gravity(moons)
        moons = apply_velocity(moons)

        state = get_state(moons)

        for i in range(len(state)):
            if state[i] == initial_state[i] and cycle_lengths[i] == 0:
                cycle_lengths[i] = iterations

        iterations += 1

    return math.lcm(*cycle_lengths)


def parse_input(file_path: str) -> list[Moon]:
    with open(file_path, "r") as file:
        moons = []
        for line in file:
            line = line.strip()[1:-1]
            x, y, z = line.split(", ")
            position = Position(int(x[2:]), int(y[2:]), int(z[2:]))
            velocity = Velocity(0, 0, 0)
            moons.append(Moon(position, velocity))
        return moons


# test case part B answer 4686774924
TEST_CASE = [
    Moon(Position(-8, -10, 0), Velocity(0, 0, 0)),
    Moon(Position(5, 5, 10), Velocity(0, 0, 0)),
    Moon(Position(2, -7, 3), Velocity(0, 0, 0)),
    Moon(Position(9, -8, -3), Velocity(0, 0, 0)),
]


def main(file_path: str):
    moons = parse_input(file_path)

    print(f"Part a: {energy_t1k(moons)}")
    print(f"Part b: {get_cycle_len(moons)}")
    # print(f"Test case: {get_cycle_len(TEST_CASE)}")


if __name__ == "__main__":
    main(INPUT_FILE)
