# Advent of Code
# Day 1, Star 1
# Take first and last numerical digit of each line, 
# concatenate them, and sum up the resulting numbers.

def main():
    inputFile = open('1.txt', 'r')
    inputLines = inputFile.readlines()

    sum = 0
    for line in inputLines:
        i = 0
        j = len(line) - 1
        firstFound = False
        lastFound = False
        while not firstFound:
            if line[i].isdigit():
                sum += 10 * int(line[i])
                firstFound = True
            i += 1
        while not lastFound:
            if line[j].isdigit():
                sum += int(line[j])
                lastFound = True
            j -= 1

    print(sum)

if __name__ == "__main__":
    main()