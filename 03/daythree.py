#!/bin/python3
import argparse
import sys
from pathlib import Path

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def find_count(lines, i, value):
    count = 0
    for line in lines:
        if line[i] == value:
            count += 1
    return count

def find_most_common(lines, i):
    ones = find_count(lines, i, '1')
    zeros = find_count(lines, i, '0')
    if ones > zeros:
        return 1
    elif zeros > ones:
        return 0
    else:
        return 'SAME'


def part1(lines, length):
    gamma = 0
    epsilon = 0
    gamma_bin = []
    epsilon_bin = []
    for i in range(length):
        most_common = find_most_common(lines, i)
        if most_common == 'SAME':
            print("We are doomed")
            exit(1)
        if most_common == 1:
            gamma_bin.append(1)
            epsilon_bin.append(0)
        else:
            gamma_bin.append(0)
            epsilon_bin.append(1)
    gamma = int(''.join(map(str, gamma_bin)),2)
    epsilon = int(''.join(map(str, epsilon_bin)),2)
    return gamma*epsilon

def part2(lines, length):
    co2 = 0
    oxy = 0
    oxy_lines = lines[:]
    co2_lines = lines[:]
    # oxy rating
    for i in range(length):
        keep = []
        most_common = find_most_common(oxy_lines, i)
        if most_common == 'SAME':
            # not doomed anymore, take ones
            most_common = 1
        for line in oxy_lines:
            if line[i] == str(most_common):
                keep.append(line)
        oxy_lines = keep[:]
        if len(oxy_lines) <= 1:
            break
    # co2 rating
    for i in range(length):
        keep = []
        most_common = find_most_common(co2_lines, i)
        if most_common == 'SAME':
            # not doomed, take zeros
            most_common = 1
        for line in co2_lines:
            if line[i] != str(most_common):
                keep.append(line)
        co2_lines = keep[:]
        if len(co2_lines) <=1:
            break
    if len(oxy_lines) == len(co2_lines) == 1:
        # sanity check succeeded
        oxy = int(oxy_lines[0],2)
        co2 = int(co2_lines[0],2)
        return co2 * oxy
    else:
        print("WE ARE DOOMED FOR SURE!!!!1elf")
        exit(1)

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
    length = len(lines[0])
    count_part_one = part1(lines, length)
    print(f"Solution Part 1: {count_part_one}")
    count_part_two = part2(lines, length)
    print(f"Solution Part 2: {count_part_two}")

if __name__ == '__main__':
    main()
