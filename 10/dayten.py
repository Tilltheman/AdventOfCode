#!/bin/python3
import argparse
import sys
from pathlib import Path
from lark import Lark
from lark.exceptions import UnexpectedCharacters, UnexpectedToken, UnexpectedEOF


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

incomplete_lines = []
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
def part1(lines):
    result = 0
    for line in lines:
        with open("grammar.lark") as g:
            parser = Lark(g)
            try:
                tree = parser.parse(line)
            except UnexpectedEOF as uEOF:
                incomplete_lines.append(line)
                continue
            except UnexpectedCharacters as e:
                uc = line[e.column-1]
                result += points.get(uc)
    return result

def complete(parser, line):
    characters = [')', ']', '}', '>']
    used_chars = []
    done = False
    linelist = list(line)
    while(not done):
        linelist.append('x')
        for c in characters:
            linelist[-1] = c
            try:
                tree = parser.parse("".join(linelist))
            except UnexpectedEOF as ue:
                used_chars.append(c)
                break
            except UnexpectedCharacters as uc:
                continue
            used_chars.append(c)
            done = True
            break
    return used_chars

points2 = {')': 1, ']': 2, '}': 3, '>': 4}
def part2(lines):
    result = 0
    line_scores = []
    for line in incomplete_lines:
        line_score = 0
        with open("grammar.lark") as g:
            parser = Lark(g)
            used_symbols = complete(parser, line)
            for char in used_symbols:
                line_score *= 5
                line_score += points2.get(char)
        line_scores.append(line_score)
    sorted_scores = sorted(line_scores)
    middle = len(sorted_scores)//2
    return sorted_scores[middle]

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
