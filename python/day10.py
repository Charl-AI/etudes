import argparse
import math
from typing import Literal, NamedTuple


class Asteroid(NamedTuple):
    x: int
    y: int


def parse_input(file_path: str) -> set[Asteroid]:
    asteroids = set()

    with open(file_path, "r") as file:
        for y, line in enumerate(file):
            for x, char in enumerate(line.strip()):
                if char == "#":
                    asteroids.add(Asteroid(x, y))
    return asteroids


def compute_visibility_matrix(
    location: Asteroid, asteroids: set[Asteroid]
) -> list[list[int]]:
    """Visibility matrix represents vectors from the location to all other asteroids."""
    a = asteroids - {location}  # remove the location from the set of asteroids

    matrix = []
    for asteroid in a:
        x, y = asteroid.x - location.x, asteroid.y - location.y
        matrix.append([x, y])
    return matrix


def compute_angle(vector: list[int]) -> float:
    return math.degrees(math.atan2(vector[1], vector[0]) + 90) % 360


def compute_distance(vector: list[int]) -> float:
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)


def compute_visibility(visibility_matrix: list[list[int]]) -> int:
    angles = set()
    for vector in visibility_matrix:
        angle = compute_angle(vector)
        angles.add(angle)
    return len(angles)


def solve_part_a(asteroids: set[Asteroid]) -> tuple[Asteroid, int]:
    highest_visibility = 0
    best_asteroid = None
    for asteroid in asteroids:
        matrix = compute_visibility_matrix(asteroid, asteroids)
        visibility = compute_visibility(matrix)
        if visibility > highest_visibility:
            highest_visibility = visibility
            best_asteroid = asteroid
    assert best_asteroid is not None
    return best_asteroid, highest_visibility


def solve_part_b(asteroids: set[Asteroid]) -> int:
    location, _ = solve_part_a(asteroids)
    visibility_matrix = compute_visibility_matrix(location, asteroids)

    asteroid_map = {}
    for vector in visibility_matrix:
        # measure angles from the top (pi/2)
        angle = compute_angle(vector)
        distance = compute_distance(vector)
        if angle not in asteroid_map:
            asteroid_map[angle] = []
        asteroid_map[angle].append((vector, distance))
    angles = reversed(sorted(asteroid_map.keys()))

    # sort vectors by distance
    for angle in asteroid_map:
        asteroid_map[angle] = sorted(asteroid_map[angle], key=lambda x: x[1])

    destroyed = 0
    while destroyed < 200:
        for angle in angles:
            if len(asteroid_map[angle]) > 0:
                vector, _ = asteroid_map[angle].pop(0)
                destroyed += 1
                if destroyed == 200:
                    return (vector[0] + location.x) * 100 + (vector[1] + location.y)


TEST_CASE = [
    [".", ".", ".", ".", ".", ".", "#", ".", "#", "."],
    ["#", ".", ".", "#", ".", "#", ".", ".", ".", "."],
    [".", ".", "#", "#", "#", "#", "#", "#", "#", "."],
    [".", "#", ".", "#", ".", "#", "#", "#", ".", "."],
    [".", "#", ".", ".", "#", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
    ["#", ".", ".", "#", ".", ".", ".", ".", "#", "."],
    [".", "#", "#", ".", "#", ".", ".", "#", "#", "#"],
    ["#", "#", ".", ".", ".", "#", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", "#", "#", "#", "#"],
]


def parse_test_input(test_array: list[list[str]]) -> set[Asteroid]:
    asteroids = set()
    for y, line in enumerate(test_array):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.add(Asteroid(x, y))
    return asteroids


def main(question: Literal["a", "b", "tests"], file_path: str):
    asteroids = parse_input(file_path)

    if question == "a":
        print(solve_part_a(asteroids))

    elif question == "b":
        print(solve_part_b(asteroids))

    elif question == "tests":
        test_1 = parse_test_input(TEST_CASE)
        print(solve_part_a(test_1))

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
