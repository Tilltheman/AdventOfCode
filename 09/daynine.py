#!/bin/python3
import argparse
import sys
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

class Point:
    """ Point has up down left right neighbors, a center value and x,y coordinates """
    def __init__(self, c, x, y, u=None, d=None, l=None, r=None):
        self.c = c
        self.x = x
        self.y = y
        self.u = u
        self.d = d
        self.l = l
        self.r = r

    def is_lower_point(self):
        if self.c < self.u.c and self.c < self.d.c and self.c < self.l.c and self.c < self.r.c:
            return True
        return False

    def risk_level(self):
        return self.c + 1

    def get_neighbors(self):
        neighbors = []
        if self.u:
            neighbors.append(self.u)
        if self.d:
            neighbors.append(self.d)
        if self.l:
            neighbors.append(self.l)
        if self.r:
            neighbors.append(self.r)
        return neighbors

    def basin_size(self, visited):
        b = 1
        neighbors = self.get_neighbors()
        for n in neighbors:
            if n.c >= 9:
                continue
            elif n.c > self.c and n not in visited:
                b += n.basin_size(visited)
                visited.append(n)
            else:
                continue
        return b

    def __str__(self):
        return f"P({self.x},{self.y},{self.c})"

points = []
def part1(lines):
    xmax = len(lines)
    ymax = len(lines[0])
    for i, line in enumerate(lines):
        points.append([])
        for j, pos in enumerate(line):
            points[i].append(Point(int(pos),i,j))
    for i in range(len(points)):
        for j in range(len(points[i])):
            if i-1 < 0:
                points[i][j].u = Point(17,-1,-1)
            else:
                points[i][j].u = points[i-1][j]
            if i+1 >= xmax:
                points[i][j].d = Point(17,-1,-1)
            else:
                points[i][j].d = points[i+1][j]
            if j-1 < 0:
                points[i][j].l = Point(17,-1,-1)
            else:
                points[i][j].l = points[i][j-1]
            if j+1 >= ymax:
                points[i][j].r = Point(17,-1,-1)
            else:
                points[i][j].r = points[i][j+1]
    result = 0
    for i in range(len(points)):
        for j in range(len(points[i])):
            if points[i][j].is_lower_point():
                result += points[i][j].risk_level()
    return result

def part2(lines):
    basin_sizes = []
    for i in range(len(points)):
        for j in range(len(points[i])):
            if points[i][j].is_lower_point():
                basin_sizes.append(points[i][j].basin_size([]))
    result = 1
    for r in sorted(basin_sizes)[-3:]:
        result *= r
    return result

def main():
    args = parse_args(sys.argv[1:])
    fname = Path(args.file)
    if not fname.is_file():
        print("please provide input data")
        exit(1)
    lines = []
    with open(fname) as indata:
        lines = indata.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    lines_part_one = lines[:]
    lines_part_two = lines[:]
    count_part_one = part1(lines_part_one)
    print(f"Solution Part 1: {count_part_one}")
    count_part_two = part2(lines_part_two)
    print(f"Solution Part 2: {count_part_two}")

if __name__ == '__main__':
    main()
