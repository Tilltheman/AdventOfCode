#!/bin/python3
import argparse
import sys
from pathlib import Path
import re
import os


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def part1(lines, steps):
    starting_pattern = lines[0]
    rules = {}
    for line in lines[2:]:
        match = re.match("(..) -> (.)", line)
        if not match:
            print("We are doomed!")
            exit(1)
        key = match.group(1)
        value = match.group(2)
        rules[key] = value
    pattern = list(starting_pattern)
    for i in range(steps):
        print(f'in step {i}')
        temp_result = []
        for j in range(len(pattern)-1):
            pair = pattern[j:j+2]
            pair[1] = rules[''.join(pair)]
            temp_result.extend(pair)
        temp_result.append(pattern[-1])
        pattern = temp_result 
    counts = {}
    for char in pattern:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    max_occurance = 0
    min_occurance = 1000000
    for k in counts:
        if counts[k] > max_occurance:
            max_occurance = counts[k]
        if counts[k] < min_occurance:
            min_occurance = counts[k]
    print(max_occurance)
    print(min_occurance)
    result = max_occurance - min_occurance
    return result

def do_it(pattern, rules):
    temp_result = []
    for j in range(len(pattern)-1):
        pair = pattern[j:j+2]
        pair[1] = rules[''.join(pair)]
        temp_result.extend(pair)
    temp_result.append(pattern[-1])
    return temp_result

POSITIONS = 100000

def do_it_in_range(pattern, steps, rules):
    for i in range(steps):
        print(f"In Step {i}")
        if len(pattern) <= POSITIONS:
            pattern = do_it(pattern, rules)
        else:
            print("Second Branch")
            print(f"LEN: {len(pattern)}")
            parts = len(pattern)//POSITIONS + 1
            lol = [[None] * POSITIONS ] * parts
            ress = [[None] * POSITIONS ] * parts
            print(f"parts {parts}")
            for i in range(parts):
                lol[i] = pattern[i*POSITIONS:(i+1)*POSITIONS]
            for i in range(parts):
                for j in range(len(lol)):
                    ress[j] = do_it(lol[j], rules)
            result = []
            for i in range(len(ress)):
                result += ress[i][:-1]
            result += ress[-1][-1]
            pattern = result
        # print(''.join(pattern))
    return pattern

def part2(lines, steps):
    starting_pattern = lines[0]
    rules = {}
    for line in lines[2:]:
        match = re.match("(..) -> (.)", line)
        if not match:
            print("We are doomed!")
            exit(1)
        key = match.group(1)
        value = match.group(2)
        rules[key] = value
    pattern_list = list(starting_pattern)
    pattern = pattern_list
    steps = 25
    result = do_it_in_range(pattern, steps, rules)

#    pattern1 = pattern_list[0:3]
#    res_4 = do_it_in_range(pattern1, steps, rules)
#    pattern1 = pattern_list[2:4]
#    res_5 = do_it_in_range(pattern1, steps, rules)
#    result1 = res_4[:-1] + res_5
#    assert result == result1
#    print(result == result1)
    print(f"len 1: {len(result)}") # len 2: {len(result1)}")
    pass

def someting():
    pattern = pattern_list[1:3]
    for i in range(steps):
        print(f'in step {i} 2')
        temp_result = []
        for j in range(len(pattern)-1):
            pair = pattern[j:j+2]
            pair[1] = rules[''.join(pair)]
            temp_result.extend(pair)
        temp_result.append(pattern[-1])
        pattern = temp_result
    res_2 = pattern
    pattern = pattern_list[2:4]
    print(pattern)
    for i in range(steps):
        print(f'in step {i} 3')
        temp_result = []
        for j in range(len(pattern)-1):
            pair = pattern[j:j+2]
            pair[1] = rules[''.join(pair)]
            temp_result.extend(pair)
        temp_result.append(pattern[-1])
        pattern = temp_result
    res_3 = pattern
    pattern = res_1 + res_2 + res_3
    counts = {}
    for char in pattern:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    max_occurance = 0
    min_occurance = 1000000
    for k in counts:
        if counts[k] > max_occurance:
            max_occurance = counts[k]
        if counts[k] < min_occurance:
            min_occurance = counts[k]
    print(max_occurance)
    print(min_occurance)
    result = max_occurance - min_occurance
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
    count_part_one = part1(lines_part_one, 10)
    print(f"Solution Part 1: {count_part_one}")
    count_part_two = part2(lines_part_two, 40)
    print(f"Solution Part 2: {count_part_two}")

if __name__ == '__main__':
    main()
