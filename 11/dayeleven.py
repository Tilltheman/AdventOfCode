#!/bin/python3
import argparse
import sys
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

octopuses = []

def procto():
    for octo in octopuses:
        print(octo)

class Octopus:
    total_flashes = 0
    def __init__(self, x, y, energy, neighbors):
        self.x = x
        self.y = y
        self.energy = energy
        self.neighbors = neighbors
        self.flashed = False

    def __str__(self):
        byte = b'\xf0\x9f\x90\x99'
        rep = byte.decode('utf-8')
        return f"{rep}({self.energy})"

    def __repr__(self):
        byte = b'\xf0\x9f\x90\x99'
        rep = byte.decode('utf-8')
        return f"{rep}({self.energy})"

    def add(self, n=1):
        self.energy += n

    def get(self):
        return self.energy

    def reset(self):
        self.energy = 0

    def flash(self):
        # we have to flash
        self.flashed = True
        Octopus.total_flashes += 1
        for neighbor in self.neighbors:
            if not neighbor.flashed:
                # neighbors get more energy
                neighbor.add()
                # check if they have to flash
                if neighbor.get() > 9:
                    neighbor.flash()
        self.reset()

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors


def find_neighbors(x, y, max_x, max_y):
    neighbors = []
    points = [(x-1,y-1), (x,y-1), (x+1,y-1),
              (x-1, y),           (x+1, y),
              (x-1,y+1), (x,y+1), (x+1, y+1)]
    copy_points = points[:]
    for p in copy_points:
        if p[0] < 0 or p[1] < 0 or p[0] >= max_x or p[1] >= max_y:
            points.remove(p)
    for p in points:
        neighbors.append(octopuses[p[0]][p[1]])
    return neighbors

def part1(lines):
    max_x = len(lines)
    max_y = len(lines[0])
    for i, line in enumerate(lines):
        octopuses.append([])
        for j, char in enumerate(line):
            o = Octopus(i,j,int(char),[])
            octopuses[i].append(o)
    for i in range(max_x):
        for j in range(max_y):
            octopuses[i][j].set_neighbors(find_neighbors(i, j, max_x, max_y))
    steps = 100
    for step in range(steps):
        # add 1 to every octopus
        for i in range(max_x):
            for j in range(max_y):
                octopuses[i][j].add()
        # now let the flashing begin
        for i in range(max_x):
            for j in range(max_y):
                if octopuses[i][j].get() > 9:
                    octopuses[i][j].flash()
        one_not_zero = False
        for i in range(max_x):
            for j in range(max_x):
                if octopuses[i][j].get() != 0:
                    one_not_zero = True
        if not one_not_zero and step_all_flashed == -1:
            step_all_flashed = step
        # reset the flashed state:
        for i in range(max_x):
            for j in range(max_y):
                octopuses[i][j].flashed = False
    return Octopus.total_flashes

def part2(lines):
    max_x = len(lines)
    max_y = len(lines[0])
    step = 0
    step_all_flashed = -1
    while step_all_flashed == -1:
        # add 1 to every octopus
        for i in range(max_x):
            for j in range(max_y):
                octopuses[i][j].add()
        # now let the flashing begin
        for i in range(max_x):
            for j in range(max_y):
                if octopuses[i][j].get() > 9:
                    octopuses[i][j].flash()
        one_not_zero = False
        for i in range(max_x):
            for j in range(max_x):
                if octopuses[i][j].get() != 0:
                    one_not_zero = True
        if not one_not_zero and step_all_flashed == -1:
            step_all_flashed = step
        # reset the flashed state:
        for i in range(max_x):
            for j in range(max_y):
                octopuses[i][j].flashed = False
        step +=1
    return 100 + step

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
