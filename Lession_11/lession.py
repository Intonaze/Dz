class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    def distance(self, second_point):
        dx = second_point.x - self.x
        dy = second_point.y - self.y
        return (dx ** 2 + dy ** 2) ** 0.5

s = Point(5, 2)