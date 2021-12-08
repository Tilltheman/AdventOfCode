#!/bin/python3
import argparse
import sys
from pathlib import Path


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

unique_segment_patterns = {1: 2, 4: 4, 7: 3, 8: 7}

def one_of_uniques(digit, part2=False):
    for u in unique_segment_patterns:
        if len(digit) == unique_segment_patterns.get(u):
            if part2:
                return True, u
            else:
                return True, -1
    return False, -17


def analyse(signal_patterns):
    digit_segments = ['','','','','','','']
    lookup = {}
    pattern_digits_mapping = {}
    patterns_length_five = []
    patterns_length_six = []
    for pattern in signal_patterns:
        oou, u = one_of_uniques(pattern, True)
        if oou:
            lookup[u] = pattern
        elif len(pattern) == 5:
            patterns_length_five.append(pattern)
        elif len(pattern) == 6:
            patterns_length_six.append(pattern)
    # 7 and 1 provide the upper segment
    digit_segments[0] = lookup[7].replace(lookup[1][0],"").replace(lookup[1][1],"")
    # from the 4 uniques we can derive something like this
    #      ddd
    #      ---
    # e/f| e/f | a/b
    #      ---
    # c/g|     | a/b
    #      ---
    #      c/g
    temp = lookup[8]
    for char in lookup[4]:
        temp = temp.replace(char, "")
    temp = temp.replace(digit_segments[0],"")
    decision_helper = {
        0: digit_segments[0],
        1: lookup[4].replace(lookup[1][0],"").replace(lookup[1][1],""),
        2: lookup[1],
        3: lookup[4].replace(lookup[1][0],"").replace(lookup[1][1],""),
        4: temp,
        5: lookup[1],
        6: temp,
    }
    fpattern1 = set(patterns_length_five[0].replace(digit_segments[0],""))
    fpattern2 = set(patterns_length_five[1].replace(digit_segments[0],""))
    fpattern3 = set(patterns_length_five[2].replace(digit_segments[0],""))
    bottom_possible = set(decision_helper[6])
    digit_segments[3] = list(((fpattern1 & fpattern2) & fpattern3) - bottom_possible)[0]
    decision_helper[1] = decision_helper[1].replace(digit_segments[3],"")
    decision_helper[3] = digit_segments[3]
    digit_segments[1] = decision_helper[1]
    for pattern in patterns_length_five:
        pattern = set(pattern)
        temp = pattern - set(digit_segments)
        l = len(temp)
        if l == 2:
            # this is the two
            decision_helper[2] = list(set(decision_helper[2]) - temp)[0]
            digit_segments[2] = decision_helper[2]
            decision_helper[5] = decision_helper[5].replace(decision_helper[2],"")
            digit_segments[5] = decision_helper[5]
            decision_helper[6] = list(pattern - set(digit_segments))[0]
            digit_segments[6] = decision_helper[6]
            decision_helper[4] = decision_helper[4].replace(decision_helper[6],"")
            digit_segments[4] = decision_helper[4]

    for i, pattern in enumerate(signal_patterns):
        if set(pattern) == set(digit_segments[0:3] + digit_segments[4:7]):
            pattern_digits_mapping[''.join(sorted(list(pattern)))] = 0
        elif set(pattern) == set([digit_segments[2]] + [digit_segments[5]]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 1
        elif set(pattern) == set([digit_segments[0]] + digit_segments[2:5] + [digit_segments[6]]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 2
        elif set(pattern) == set([digit_segments[0]] + digit_segments[2:4] +digit_segments[5:7]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 3
        elif set(pattern) == set(digit_segments[1:4] + [digit_segments[5]]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 4
        elif set(pattern) == set(digit_segments[0:2] + [digit_segments[3]] + digit_segments[5:7]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 5
        elif set(pattern) == set(digit_segments[0:2] + digit_segments[3:7]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 6
        elif set(pattern) == set([digit_segments[0]] + [digit_segments[2]] + [digit_segments[5]]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 7
        elif set(pattern) == set(digit_segments):
            pattern_digits_mapping[''.join(sorted(pattern))] = 8
        elif set(pattern) == set(digit_segments[0:4] + digit_segments[5:7]):
            pattern_digits_mapping[''.join(sorted(pattern))] = 9
    return pattern_digits_mapping

def decode(digits, signal_patterns):
    result_list = [0,0,0,0]
    mapping = analyse(signal_patterns)
    for i, digit in enumerate(digits):
        digit_list = list(set([x for x in digit]))
        key = ''.join(sorted(digit_list))
        result_list[i] = mapping[key]
    return int(''.join([str(r) for r in result_list]))

def part1(lines):
    overall = 0
    for line in lines:
        signal_patterns_input = line.split('|')[0]
        digit_output = line.split('|')[1]
        signal_patterns = signal_patterns_input.split()
        digits = digit_output.split()
        for digit in digits:
            if one_of_uniques(digit)[0]:
                overall += 1
    return overall

def part2(lines):
    overall = 0
    for line in lines:
        signal_patterns_input = line.split('|')[0]
        digit_output = line.split('|')[1]
        signal_patterns = signal_patterns_input.split()
        digits = digit_output.split()
        result = decode(digits, signal_patterns)
        overall += result
    return overall

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
