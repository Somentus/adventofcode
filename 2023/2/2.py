# Advent of Code
# Day 2 Star 2

def sumOf(minimum):
    return minimum["red"] * minimum["green"] * minimum["blue"]

def main():
    inputFile = open('1.txt', 'r')
    inputLines = inputFile.readlines()

    sum = 0

    for line in inputLines:
        minimum = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        line = line.strip()
        line = line.replace("Game ", "")
        line = line.split(': ')[1]
        
        for series in line.split('; '):
            for draw in series.split(', '):
                number = int(draw.split(" ")[0])
                colour = draw.split(" ")[1]
                
                if minimum[colour] < number:
                    minimum[colour] = number
        sum += sumOf(minimum)
    print(sum)

if __name__ == "__main__":
    main()
