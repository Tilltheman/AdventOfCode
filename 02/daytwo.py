#!/bin/python3
import argparse
import sys
from pathlib import Path

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def part1(lines):
    x = 0
    y = 0

    for line in lines:
        distance = int(line.split()[1])
        if line.startswith("f"):
            # forward
            x += distance
        elif line.startswith("u"):
            # up
            y -= distance
        elif line.startswith("d"):
            # down
            y += distance
        else:
            exit(1)
    return x*y

def part2(lines):
    x = 0
    y = 0
    aim = 0

    for line in lines:
        distance = int(line.split()[1])
        if line.startswith("f"):
            # forward
            x += distance
            y += aim * distance
        elif line.startswith("u"):
            # up
            aim -= distance
        elif line.startswith("d"):
            # down
            aim += distance
        else:
            exit(1)
    return x*y

def main():
    args = parse_args(sys.argv[1:])
    fname = Path(args.file)
    if not fname.is_file():
        print("please provide input data")
        exit(1)
    lines = []
    with open(fname) as indata:
        lines = indata.readlines()
    count_part_one = part1(lines)
    print(f"Solution Part 1: {count_part_one}")
    count_part_two = part2(lines)
    print(f"Solution Part 2: {count_part_two}")

if __name__ == '__main__':
    main()
