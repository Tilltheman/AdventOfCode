#!/bin/python3
import argparse
import sys
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def part1(lines, part2=False):
    initial_positions = [int(p) for p in lines[0].split(",")]
    maximum = max(initial_positions)
    fuels = []
    for i in range(maximum):
        fuel = 0
        for pos in initial_positions:
            if(part2):
                n = abs(pos-i)
                fuel += int((n*(n+1))/2)
            else:
                fuel += abs(pos-i)
        fuels.append(fuel)
    return min(fuels)

def part2(lines):
    return part1(lines, True)

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
