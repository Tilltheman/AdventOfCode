#!/bin/python3
import argparse
import sys
from pathlib import Path

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def part1(lines):
    previous = sys.maxsize
    count = 0
    for line in lines:
        line = int(line)
        if previous < line:
            count += 1
        previous = line
    return count

def part2(lines):
    previous_sum = sys.maxsize
    count = 0
    sums = []
    for i in range(len(lines)-2):
        s = sum(int(l) for l in lines[i:i+3])
        sums.append(s)
    count = part1(sums)
    return count

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
