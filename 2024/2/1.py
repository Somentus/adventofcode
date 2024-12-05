# Advent of Code
# Day 2, Star 1
# Output how many reports are safe.
# Input consists of lines, each line is a report containing multiple levels.
# A report is safe if it consists of only increasing or only decreasing levels
# Any adjacent levels must differ by at least 1 and at most 3

from __future__ import annotations

def jumpIsAllowed(left: int, right: int):
    if abs(left - right) <= 3 and abs(left - right) >= 1:
        return True
    return False

def isSafe(report: list[int]):
    increasing: bool = False
    previous = report[0]
    current = report[1]
    if previous < current:
        increasing = True
    else:
        increasing = False
    if not jumpIsAllowed(previous, current):
        return False
    for index in range(2, len(report)):
        previous = current
        current = report[index]
        if previous > current and increasing or (previous < current and not increasing):
            return False
        if not jumpIsAllowed(previous, current):
            return False
    return True

def main():
    inputFile = open('1.in', 'r')
    inputLines = inputFile.readlines()

    sum = 0
    report: list[int] = []
    for line in inputLines:
        report = [int(val) for val in line.split()]
        if isSafe(report):
            sum += 1

    print(sum)

if __name__ == "__main__":
    main()