# Advent of Code
# Day 1, Star 2
# Take first and last numerical or written out 
# digit of each line, concatenate them, 
# and sum up the resulting numbers.

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
stringToNumber = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def main():
    inputFile = open('1.txt', 'r')
    inputLines = inputFile.readlines()

    sum = 0
    for line in inputLines:
        firstPosition = len(line)
        firstNumber = 0
        lastPosition = -1
        lastNumber = 0
        for digit in digits:
            firstFound = line.find(digit)
            lastFound = line.rfind(digit)
            if firstFound > -1 and firstFound < firstPosition:
                firstPosition = firstFound
                firstNumber = stringToNumber[digit]
            if lastFound > -1 and lastFound > lastPosition:
                lastPosition = lastFound
                lastNumber = stringToNumber[digit]
        sum += firstNumber * 10
        sum += lastNumber
    print(sum)

if __name__ == "__main__":
    main()
