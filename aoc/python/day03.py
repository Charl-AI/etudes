from typing import List, Tuple

INPUT_FILE = "data/2019/day03.txt"


def get_inputs(file_path: str) -> List[List[str]]:
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip().split(","))
    return lines


def parse_line(line: List[str]) -> List[Tuple[int, int]]:
    """Parse a list of string representations of the segments e.g. 'R120' to a dense,
    ordered list of the points the line passes through"""

    coords: List[Tuple[int, int]] = [(0, 0)]

    for segment in line:
        direction = segment[0]
        distance = int(segment[1:])

        if direction == "R":
            coords.extend(
                [(coords[-1][0] + i, coords[-1][1]) for i in range(1, distance + 1)]
            )
        elif direction == "L":
            coords.extend(
                [(coords[-1][0] - i, coords[-1][1]) for i in range(1, distance + 1)]
            )
        elif direction == "U":
            coords.extend(
                [(coords[-1][0], coords[-1][1] + i) for i in range(1, distance + 1)]
            )
        elif direction == "D":
            coords.extend(
                [(coords[-1][0], coords[-1][1] - i) for i in range(1, distance + 1)]
            )

    return coords


def steps_to_vertex(line_coords: List[Tuple[int, int]], vertex: Tuple[int, int]):
    return line_coords.index(vertex)


def combined_steps_to_vertex(
    line_1_coords: List[Tuple[int, int]],
    line_2_coords: List[Tuple[int, int]],
    vertex: Tuple[int, int],
):
    line_1_steps = steps_to_vertex(line_1_coords, vertex)
    line_2_steps = steps_to_vertex(line_2_coords, vertex)
    return line_1_steps + line_2_steps


def main(file_path: str):
    lines = get_inputs(file_path)
    assert len(lines) == 2
    line_1_coords = parse_line(lines[0])
    line_2_coords = parse_line(lines[1])

    intersections = set(line_1_coords) & set(line_2_coords)

    manhattan_distances = list(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
    manhattan_distances.remove(0)

    print("Solution to part a:")
    print(min(manhattan_distances))

    sum_distances = list(
        map(
            lambda x: combined_steps_to_vertex(line_1_coords, line_2_coords, x),
            intersections,
        )
    )
    sum_distances.remove(0)
    print("Solution to part b:")
    print(min(sum_distances))


if __name__ == "__main__":
    main(INPUT_FILE)
