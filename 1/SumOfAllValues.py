def isNumber(char):
    try:
        val = int(char)
        return True
    except ValueError:
        return False

def getAllValues(txt):
    lines = []
    with open(txt) as f:
        lines = f.readlines()
    allValues = []
    for line in lines:
        firstDigit = None
        secondDigit = None
        for char in line:
            if isNumber(char):
                if(firstDigit == None and secondDigit == None):
                    firstDigit = char
                    secondDigit = char
                else:
                    secondDigit = char
        allValues.append(str(firstDigit)+str(secondDigit))
    return allValues

def sumAllValues(values):
    sum = 0
    for value in values:
        sum+=int(value)
    
    return sum

    
allValues = getAllValues('1/input.txt')
sum = sumAllValues(allValues)
print(sum)

