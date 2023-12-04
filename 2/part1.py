LOADED_BAG = {'blue': 14, 'red': 12, 'green': 13}

def lineToDict(line):
    segments = line.split(';')
    result = []

    for segment in segments:
        if segment.strip():  # Check if the segment is not just empty spaces
            pairs = segment.split(',')
            segment_dict = {}

            for pair in pairs:
                color, count = pair.strip().split(' ')
                segment_dict[color] = int(count)

            result.append(segment_dict)

    return result


def getLines(file):
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines

def checkPossible(game):
    for key in LOADED_BAG:
        if(game[key] > LOADED_BAG[key]):
            return False
    return True



def main():
    lines = getLines('2/input.txt')

main()