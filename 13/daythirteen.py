#!/bin/python3
import argparse
import sys
from pathlib import Path
import re


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def part1(lines):
    reached_folds = False
    dot_coordinates = []
    fold_instructions = []
    for line in lines:
        if line == "":
            reached_folds = True
            continue
        if not reached_folds:
            # Handle input as coordinates
            dot_coordinates.append(line)
        else:
            # Handle input as fold instruction
            fold_instructions.append(line)
    max_x = 0
    max_y = 0
    for dot in dot_coordinates:
        x,y = dot.split(',')
        x, y = int(x), int(y)
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
    print(max_x, max_y)
    coordinates = []
    for i in range(max_y + 1):
        coordinates.append([])
        for j in range(max_x +1):
            coordinates[i].append(0)
    for dot in dot_coordinates:
        x,y = dot.split(",")
        x, y = int(x), int(y)
        coordinates[y][x] = 1
    for instruction in fold_instructions:
        print(instruction)
        match = re.match("fold along ([yx])=(\d+)", instruction)
        if not match:
            print("we are doomed")
            exit(1)
        axis = match.group(1)
        value = int(match.group(2))
        print(axis, value)
        if axis == 'y':
            x = value
            for i, v in enumerate(coordinates[x]):
                for j in range(x+1):
                    coordinates[value-j][i] += coordinates[value+j][i]
            for k in range(x, max_y+1):
                try:
                    l = coordinates.pop(k)
                except IndexError:
                    pass
        elif axis == 'x':
            y = value
            for i in range(len(coordinates)):
                for j in range(y+1):
                    try:
                        coordinates[i][value-j] += coordinates[i][value+j]
                    except IndexError:
                        pass
            for i in range(len(coordinates)):
                for k in range(y+1,max_x+2):
                    try:
                        coordinates[i].pop(k)
                    except IndexError:
                        pass
    count = 0
    for cc in coordinates:
        print(''.join( "." if x == 0 else "#" for x in cc))
        for i in cc:
            count += 1 if i != 0 else 0
    return count

def part2(lines):
    return len(lines)

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
