import enum


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


BASIS = {
    Direction.NORTH: (0, 1),
    Direction.EAST: (1, 0),
    Direction.SOUTH: (0, -1),
    Direction.WEST: (-1, 0),
}


def robot_sim(commands: list[int], obstacles: list[list[int]]) -> int:
    res = 0
    x, y = 0, 0
    dir = Direction.NORTH
    obs = {tuple(coords) for coords in obstacles}

    for command in commands:
        if command == -1:  # turn right
            dir = Direction((dir.value + 1) % 4)
        elif command == -2:  # turn left
            dir = Direction((dir.value - 1) % 4)
        else:
            dx, dy = BASIS[dir]
            for _ in range(command):
                if (x + dx, y + dy) in obs:  # blocked: stay put
                    break
                x += dx
                y += dy
            dist = x**2 + y**2
            res = max(res, dist)

    return res


assert robot_sim([4, -1, 3], obstacles=[]) == 25
assert robot_sim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]) == 65
assert robot_sim(commands=[6, -1, -1, 6], obstacles=[[0, 0]]) == 36
