import sys


def read_circle(file_path) -> tuple[int, int, int]:
    """A function that reads the coordinates of
    the center of a circle and its radius."""

    with open(file_path, 'r') as file:
        lines = [line.strip().split() for line in file.readlines()]
        x = int(lines[0][0])
        y = int(lines[0][1])
        radius = int(lines[1][0])

    return x, y, radius


def read_points(file_path) -> list:
    """A function that reads the coordinates of points."""

    with open(file_path, 'r') as f:
        points = [list(map(int, line.split())) for line in f.readlines()]
    return points


def calculate_position(circle, point) -> int:
    """A function that calculates the position of a point relative to a circle."""

    x, y, radius = circle
    px, py = point
    distance = ((px - x) ** 2 + (py - y) ** 2) ** 0.5
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print('Usage: python task2.py <circle_file> <points_file>')
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle = read_circle(circle_file)
    points = read_points(points_file)

    for point in points:
        position = calculate_position(circle, point)
        print(position)


if __name__ == '__main__':
    main()
