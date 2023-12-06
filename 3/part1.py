import re

SYMBOL_REGEX = r'[^\w\d\s.]'
NUMBER_REGEX = r'[0-9]'

def getLines(file):
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines

def findNumberRanges(index_list):
    if not index_list or not isinstance(index_list[0], int):
        return []
    ranges = []
    start = index_list[0]

    for i in range(1, len(index_list)):
        if index_list[i] != index_list[i - 1] + 1:
            end = index_list[i - 1]
            ranges.append((start, end))
            start = index_list[i]
    ranges.append((start, index_list[-1]))

    return ranges

def isNearSymbol(numIndexRange, symbolLineIndex):
    for symbol in symbolLineIndex:
        if(symbol >= numIndexRange[0]-1 and symbol <= numIndexRange[1]+1):
            return True
    return False

def main():
    lines = getLines('3/input.txt')
    numbers = []
    symbols = []

    total = 0

    numberStartAndEndIndexes = []
    for line in lines:
        symbols.append([m.start() for m in re.finditer(SYMBOL_REGEX, line)])
        numbers.append([m.start() for m in re.finditer(NUMBER_REGEX, line)])
    for num in numbers:
        numberStartAndEndIndexes.append(findNumberRanges(num))
    
    for i, num in enumerate(numberStartAndEndIndexes):
            for set in num:
                if i + 1 < len(symbols) and isNearSymbol(set, symbols[i + 1]):
                    total += int(lines[i][set[0]:set[1]+1])
                elif i - 1 < len(symbols) and isNearSymbol(set, symbols[i - 1]):
                    total += int(lines[i][set[0]:set[1]+1])
                elif isNearSymbol(set, symbols[i]):
                    total += int(lines[i][set[0]:set[1]+1])
    print(total)
main()