# Advent of Code
# Day 2, Star 1
# Sum of: each number in left list multiplied by number of occurences of said number in right list

def main():
    inputFile = open('1.in', 'r')
    inputLines = inputFile.readlines()

    sum = 0
    listL: list[int] = []
    listR: list[int] = []
    for line in inputLines:
        left, right = (int(val) for val in line.split())
        listL.append(left)
        listR.append(right)

    listL.sort()
    listR.sort()

    for index in range(0, len(listL)):
        sum += listL[index] * listR.count(listL[index])

    print(sum)

if __name__ == "__main__":
    main()
