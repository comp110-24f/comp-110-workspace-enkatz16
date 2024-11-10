class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx


p0: Point = Point(10.0, 0.0)
p0.translate_x(-5.0)
print(p0.dist_from_origin())


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y
        return (x_diffs**2 + y_diffs**2) ** 0.5

    def get_slope(self) -> float:
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y
        return y_diffs / x_diffs


p1: Point = Point(2.0, 1.0)
p2: Point = Point(7.0, 5.0)
path: Line = Line(p1, p2)
print(path.get_length)
