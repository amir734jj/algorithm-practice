# https://leetcode.com/problems/max-points-on-a-line/

import itertools
import math


def same_line(points):
    if len(points) > 1:
        x0, y0 = points[0]
        points = [(x, y) for x, y in points if x != x0 or y != y0]
        slopes = [(y - y0) / (x - x0) if x != x0 else math.inf for x, y in points]
        return all(slope == slopes[0] for slope in slopes)
    else:
        return True


def all_mpo(all_points):
    for count in range(len(all_points), 2, -1):
        for points in list(itertools.combinations(all_points, count)):
            if same_line(points):
                yield count


def mpo(points):
    return max(all_mpo(points))


table = [
    ([(1, 1), (2, 2), (3, 3)], 3),
    ([(1, 1), (3, 2), (5, 3), (4, 1), (2, 3), (1, 4)], 4)
]

print(list(filter(bool, [s for s, r in table if mpo(s) != r])))
