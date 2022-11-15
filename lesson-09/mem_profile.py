from memory_profiler import profile

N = 100_000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y


def process_list(lst):
    for obj in lst:
        z = obj.x + obj.y
        obj.x += obj.y
        obj.y = z


@profile
def run():
    points = [Point(5, 1) for _ in range(N)]
    slot_points = [PointSlots(5, 1) for _ in range(N)]

    process_list(points)
    process_list(slot_points)

    del points
    del slot_points

    return None


if __name__ == "__main__":
    run()



