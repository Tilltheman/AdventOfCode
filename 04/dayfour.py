#!/bin/python3
import argparse
import sys
from pathlib import Path

BOARDS = {}

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to the input')
    return parser.parse_args(args)

def score(board, drawn_numbers):
    score = 0
    for line in board:
        for item in line:
            if item not in drawn_numbers:
                score += item
    return score * drawn_numbers[-1]

def is_line_full(line, drawn_numbers):
    for element in line:
        if element not in drawn_numbers:
            return False
    return True

def is_winning(board, drawn_numbers):
    for line in board:
        if is_line_full(line, drawn_numbers):
            return True
    for i in range(len(board[0])):
        row = [item[i] for item in board]
        if is_line_full(row, drawn_numbers):
            return True
    return False

def part1(lines):
    all_drawn_numbers = [int(item) for item in lines[0].split(',')]
    number_boards = int((len(lines)-1)/6)
    board_lines = lines[1:]
    sc = 0
    for i in range(number_boards):
        BOARDS[i] = []
        for line in board_lines[(i*6)+1:(i+1)*6]:
            BOARDS[i].append([int(item) for item in line.split()])
    for i in range(len(all_drawn_numbers)):
        drawn_numbers = all_drawn_numbers[:i]
        for j in BOARDS:
            winning = is_winning(BOARDS[j], drawn_numbers)
            if winning:
                sc = score(BOARDS[j], drawn_numbers)
                print(f"Winning Board: {j+1}")
                return sc

def part2(lines):
    all_drawn_numbers = [int(item) for item in lines[0].split(',')]
    number_boards = int((len(lines)-1)/6)
    board_lines = lines[1:]
    board_won_in_round = {}
    sc = 0
    for i in range(number_boards):
        BOARDS[i] = []
        for line in board_lines[(i*6)+1:(i+1)*6]:
            BOARDS[i].append([int(item) for item in line.split()])
    for i in range(len(all_drawn_numbers)):
        drawn_numbers = all_drawn_numbers[:i]
        for j in BOARDS:
            winning = is_winning(BOARDS[j], drawn_numbers)
            if winning:
                sc = score(BOARDS[j], drawn_numbers)
                if i < board_won_in_round.get(j,(5000,1))[0]:
                    board_won_in_round[j] = (i, sc)
    last = 0
    last_board_index = 0
    for i in board_won_in_round:
        if board_won_in_round[i][0] > last:
            last = board_won_in_round[i][0]
            last_board_index = i
    return board_won_in_round[last_board_index][1]

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
