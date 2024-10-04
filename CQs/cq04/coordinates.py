"""File for coordinates function"""

__author__ = "730748249"


def get_coords(xs: str, ys: str) -> None:
    x_index: int = 0
    x_coord: str = ""
    y_coord: str = ""
    while x_index < len(xs):
        x_coord = xs[x_index]
        x_index = x_index + 1
        y_index: int = 0
        while y_index < len(ys):
            y_coord = ys[y_index]
            y_index = y_index + 1
            print(f"({x_coord},{y_coord})")
