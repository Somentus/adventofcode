# Advent of Code
# Day 2 Star 1

limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def main():
    inputFile = open('1.txt', 'r')
    inputLines = inputFile.readlines()

    validGames = set()

    for line in inputLines:
        gameValid = True

        line = line.strip()
        line = line.replace("Game ", "")
        
        id = int(line.split(': ')[0])
        validGames.add(id)

        line = line.split(': ')[1]
        
        for series in line.split('; '):
            if not gameValid:
                break
            for draw in series.split(', '):
                number = int(draw.split(" ")[0])
                colour = draw.split(" ")[1]
                
                if limit[colour] < number:
                    gameValid = False
                    validGames.remove(id)
                    break
    
    print(sum(validGames))

if __name__ == "__main__":
    main()
