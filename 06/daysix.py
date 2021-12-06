#!/bin/python3
import argparse
import sys
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def part1(lines, days):
    initial_state = lines[0].split(",")
    initial_list = [int(s) for s in initial_state]
    print(f"Initial state: {','.join(str(s) for s in initial_list)}")
    for i in range(days):
        copy_list = initial_list[:]
        for j, element in enumerate(copy_list):
            if element > 0:
                initial_list[j] -= 1
            elif element == 0:
                initial_list[j] = 6
                initial_list.append(8)
            else:
                print("We are doomed")
    return len(initial_list)

def part2(lines, days):
    initial = [int(l) for l in lines[0].split(",")]
    counts = [initial.count(x) for x in range(9)]
    print(counts)
    for _ in range(days):
        offspring = counts.pop(0)
        counts[6] += offspring
        counts.append(offspring)
    return sum(list(counts))

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
    count_part_one = part1(lines_part_one, 80)
    print(f"Solution Part 1: {count_part_one}")
    count_part_two = part2(lines_part_two, 256)
    print(f"Solution Part 2: {count_part_two}")

if __name__ == '__main__':
    main()
