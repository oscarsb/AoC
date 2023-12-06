import re

NUMBERS_AS_TEXT = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numberDict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def isNumber(char):
    try:
        val = int(char)
        return True
    except ValueError:
        return False

def getLines(txt):
    lines = []
    with open(txt) as f:
        lines = f.readlines()
    return lines
    
def getValues():
    values = []
    lines = getLines('1/input.txt')
    for line in lines:
        numbers = {}
        digits = {}
        for num in NUMBERS_AS_TEXT:
            indexes = [m.start() for m in re.finditer(num, line)]
            for index in indexes:
                if (index != -1):
                    numbers[index] = num
        for char in line:
            if(isNumber(char)):
                indexes = [m.start() for m in re.finditer(char, line)]
                for index in indexes:
                    if(index != -1):
                        digits[index] = char

        smallestKeyNumber = None
        for key in numbers:
            if(smallestKeyNumber == None):
                smallestKeyNumber = key
            elif(key < smallestKeyNumber):
                smallestKeyNumber = key

        smallestKeyDigit = None
        for key in digits:
            if(smallestKeyDigit == None):
                smallestKeyDigit = key
            elif(key < smallestKeyDigit):
                smallestKeyDigit = key

        firstValue = None
        if(smallestKeyNumber == None):
            firstValue = digits[smallestKeyDigit]
        elif(smallestKeyDigit == None):
            firstValue = numbers[smallestKeyNumber]
        elif(smallestKeyDigit < smallestKeyNumber):
            firstValue = digits[smallestKeyDigit]
        else:
            firstValue = numberDict[numbers[smallestKeyNumber]]

        biggestKeyNumber = None
        for key in numbers:
            if(biggestKeyNumber == None):
                biggestKeyNumber = key
            elif(key > biggestKeyNumber):
                biggestKeyNumber = key

        biggestKeyDigit = None
        for key in digits:
            if(biggestKeyDigit == None):
                biggestKeyDigit = key
            elif(key > biggestKeyDigit):
                biggestKeyDigit = key

        secondValue = None
        if(biggestKeyNumber == None):
            secondValue = digits[biggestKeyDigit]
        elif(biggestKeyDigit == None):
            secondValue = numbers[biggestKeyNumber]
        elif(biggestKeyDigit > biggestKeyNumber):
            secondValue = digits[biggestKeyDigit]
        else:
            secondValue = numberDict[numbers[biggestKeyNumber]]
        values.append(int(str(firstValue)+str(secondValue)))
    return values


def sumAllValues(values):
    sum = 0
    for value in values:
        sum+=int(value)
    
    return sum

values = getValues()
sum = sumAllValues(values)
print(sum)


