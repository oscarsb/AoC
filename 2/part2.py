LOADED_BAG = {'blue': 14, 'red': 12, 'green': 13}

def lineToDict(line):
    values = line.split(':')
    segments = values[1].split(';')
    result = []

    for segment in segments:
        if segment.strip():
            pairs = segment.split(',')
            segment_dict = {}

            for pair in pairs:
                count, color = pair.strip().split(' ')
                segment_dict[color] = int(count)

            result.append(segment_dict)
    return result

def getLines(file):
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines

def checkPossible(game):
    for key in game:
        if(game[key] > LOADED_BAG[key]):
            return False
    return True

def main():
    lines = getLines('2/input.txt')
    total = 0
    for line in lines:
        dictArray = lineToDict(line)
        maxBlue = 0
        maxRed = 0
        maxGreen = 0
        for lineDict in dictArray:
            if('blue' in lineDict and maxBlue < int(lineDict['blue'])):
                maxBlue = int(lineDict['blue'])
            if('green' in lineDict and maxGreen < int(lineDict['green'])):
                maxGreen = int(lineDict['green'])
            if('red' in lineDict and maxRed < int(lineDict['red'])):
                maxRed = int(lineDict['red'])
        total += maxRed*maxBlue*maxGreen
    print(total)
main()