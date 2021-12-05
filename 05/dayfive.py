#!/bin/python3
import argparse
import sys
import re
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

    
def fill_diagram(diagram, x1, y1, x2, y2, parttwo=False):
    if x1 == x2:
        # horizontal
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            diagram[x1][y] += 1
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        # vertical
        for x in range(x1, x2+1):
            diagram[x][y1] += 1
    if parttwo:
        # diagonal
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x2 != x1:
            m = (y2 - y1)/(x2 - x1)
            if abs(m) == 1:
                for x in range(x1, x2+1):
                    m = int(m)
                    diagram[x][int(m*x+((y1*x2-y2*x1)/(x2-x1)))] += 1
    return

def count_diagram_two_or_more(diagram):
    count = 0
    for line in diagram:
        for element in line:
            if element >= 2:
                count += 1
    return count

REGEX = "(\d+),(\d+) -> (\d+),(\d+)"
def part1(lines):
    max_x = 0
    max_y = 0
    diagram = []
    # get the maximum for x and y
    for line in lines:
        match = re.match(REGEX, line)
        if not match:
            print("We are doomed")
            exit(1)
        x1, y1, x2, y2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        if x1 > max_x:
            max_x = x1
        elif x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        elif y2 > max_y:
            max_y = y2
    # hold data
    max_x += 1
    max_y += 1
    for i in range(max_x):
        diagram.append([])
        for j in range(max_y):
            diagram[i].append(0)
    # fill data
    for line in lines:
        match = re.match(REGEX, line)
        if not match:
            print("We are doomed twice")
            exit(1)
        x1, y1, x2, y2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        fill_diagram(diagram, x1, y1, x2, y2)
    return count_diagram_two_or_more(diagram)

def part2(lines):
    max_x = 0
    max_y = 0
    diagram = []
    # get the maximum for x and y
    for line in lines:
        match = re.match(REGEX, line)
        if not match:
            print("We are doomed")
            exit(1)
        x1, y1, x2, y2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        if x1 > max_x:
            max_x = x1
        elif x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        elif y2 > max_y:
            max_y = y2
    # hold data
    max_x += 1
    max_y += 1
    for i in range(max_x):
        diagram.append([])
        for j in range(max_y):
            diagram[i].append(0)
    # fill data
    for line in lines:
        match = re.match(REGEX, line)
        if not match:
            print("We are doomed twice")
            exit(1)
        x1, y1, x2, y2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        fill_diagram(diagram, x1, y1, x2, y2, True)

    return count_diagram_two_or_more(diagram)

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
