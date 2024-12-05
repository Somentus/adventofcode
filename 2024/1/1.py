# Advent of Code
# Day 1, Star 1
# Compute the distance between the smallest numbers in each list
# Sum up these distances

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
        left = listL[index]
        right = listR[index]
        sum += max(left, right) - min(left, right)

    print(sum)

if __name__ == "__main__":
    main()
