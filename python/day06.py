from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

INPUT_FILE = "data/2019/day06.txt"


@dataclass
class Planet:
    name: str
    children: list[Planet] | None = None


def get_root_node(orbit_map: dict[str, Planet]) -> Planet:
    for planet in orbit_map.values():
        if planet.name == "COM":
            return planet
    raise ValueError("No root node found")


def parse_orbit_map(file_path: str) -> Planet:
    orbit_map = {}

    with open(file_path, "r") as file:
        for line in file:
            parent_name, child_name = line.strip().split(")")
            if parent_name not in orbit_map:
                orbit_map[parent_name] = Planet(parent_name)
            if child_name not in orbit_map:
                orbit_map[child_name] = Planet(child_name)

            parent = orbit_map[parent_name]
            child = orbit_map[child_name]

            if parent.children is None:
                parent.children = [child]
            else:
                parent.children.append(child)

    return get_root_node(orbit_map)


def count_orbits(root: Planet, depth: int = 0) -> int:
    if root.children is None:
        return depth
    return depth + sum(map(lambda child: count_orbits(child, depth + 1), root.children))


def get_path_to_root(planet: Planet, root: Planet) -> list[str]:
    """DFS to find the from root to the planet, returning the list of planets on the path."""

    if root.children is None:
        return []
    for child in root.children:
        if child.name == planet.name:
            return [root.name] + get_path_to_root(planet, child)
    for child in root.children:
        path = get_path_to_root(planet, child)
        if path:
            return [root.name] + path
    return []


def distance_to_santa(root: Planet) -> int:
    root_to_you = get_path_to_root(Planet("YOU"), root)
    root_to_santa = get_path_to_root(Planet("SAN"), root)
    return len(set(root_to_you) ^ set(root_to_santa))


def main(file_path: str):
    root = parse_orbit_map(file_path)

    print("Solution to part a:")
    print(count_orbits(root))

    print("Solution to part b:")
    print(distance_to_santa(root))


if __name__ == "__main__":
    main(INPUT_FILE)
