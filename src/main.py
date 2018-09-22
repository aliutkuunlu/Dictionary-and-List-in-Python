import sys

newShiftBin = []
hexList = []
charList = []
alphaList = []
reversedSecondInput = {}
shiftAmount = 0
in2LineCount = 0
hurap = sys.argv[1]
firstInput = open(hurap, "r")

shuckscii = sys.argv[2]
secondInput = {}
charTable = open(shuckscii, "r")
for letter in charTable.readlines():
    letter = letter.rstrip("\n")
    tokens = letter.split("\t")
    secondInput[tokens[1]] = tokens[0]
    alphaList.append(tokens[0])
    reversedSecondInput[tokens[0]] = tokens[1]
    in2LineCount += 1

virus = sys.argv[3]
thirdInput = {}
virusTable = open(virus, "r")
for element in virusTable.readlines():
    element = element.strip("\n")
    tokens = element.split(":")
    thirdInput[tokens[0]] = tokens[1]

hexMap = {"0000": "0",
          "0001": "1",
          "0010": "2",
          "0011": "3",
          "0100": "4",
          "0101": "5",
          "0110": "6",
          "0111": "7",
          "1000": "8",
          "1001": "9",
          "1010": "A",
          "1011": "B",
          "1100": "C",
          "1101": "D",
          "1110": "E",
          "1111": "F"
          }
binMap = {"0": "0000",
          "1": "0001",
          "2": "0010",
          "3": "0011",
          "4": "0100",
          "5": "0101",
          "6": "0110",
          "7": "0111",
          "8": "1000",
          "9": "1001",
          "A": "1010",
          "B": "1011",
          "C": "1100",
          "D": "1101",
          "E": "1110",
          "F": "1111"
         }
print("*********************")
print("     Mission 00 ")
print("*********************")
print("")
print("--- hex of encrypted code ---")
print("-----------------------------")
print("")
for numbers in firstInput.readlines():
    numbers = numbers.rstrip("\n")
    digitCount = 0
    lineSize = len(numbers) - 1
    values = []
    if numbers[0] == "0" or numbers[0] == "1":
        for i in range(lineSize // 4 + 1):
            s = numbers[digitCount:digitCount + 4]
            sys.stdout.write(hexMap[s])
            values.append(hexMap[s])
            digitCount += 4
        print("")
    else:
        if numbers[1] == "1":
            size = len(numbers[1:])
            shiftBin = numbers[1:]
            numCount = 0
            nums = []
            for items in shiftBin:
                if items == "1":
                    nums.append("0")
                else:
                    nums.append("1")
            shiftBin = bin(int(''.join(map(str, nums)), 2))
            shiftAmount = int(shiftBin, 2) + 1
        else:
            shiftBin = numbers[1:]
            shiftAmount = int(shiftBin, 2)

    if not values:
        continue
    else:
        hexList.append(values)
print("")
print("--- encrypted code ----")
print("-----------------------")
print("")
for items in hexList:
    size = len(items)
    letterCount = 0
    chars = []
    for j in range(size // 2):
        s = items[letterCount] + items[letterCount + 1]
        sys.stdout.write(secondInput[s])
        chars.append(secondInput[s])
        letterCount += 2
    charList.append(chars)
    print("")

print("")
print("--- decrypted code ---")
print("----------------------")
print("")

for item in charList:
    size = len(item)
    for i in range(size):
        index = alphaList.index(item[i])
        originIndex = (index - shiftAmount) % in2LineCount
        item[i] = alphaList[originIndex]

for item in charList:
    size = len(item)
    for i in range(size):
        sys.stdout.write(item[i])
    print("")

print("")
print("*********************")
print("     Mission 01 ")
print("*********************")
print("")
resultList = []
resultSize = 0
for line in charList:
    lines = "".join(line)
    lines = str(lines)
    for keys in thirdInput.keys():
        if keys in lines:
            lines = lines.replace(str(keys), str(thirdInput[keys]))
    resultList.append(lines)
    resultSize += 1
    print(lines)

print("")
print("*********************")
print("     Mission 10 ")
print("*********************")
print("")
print("--- encrypted code ---")
print("----------------------")
print("")

crypList = []
for element in resultList:
    size = len(element)
    listed = []
    for i in range(size):
        index = alphaList.index(element[i])
        originIndex = (index + shiftAmount) % in2LineCount
        listed.append(alphaList[originIndex])
    crypList.append(listed)

for lines in crypList:
    size = len(lines)
    for i in range(size):
        sys.stdout.write(lines[i])
    print("")

print("")
print("--- hex of encrypted code ---")
print("-----------------------------")
print("")

hexedList = []
for items in crypList:
    size = len(items)
    offset = []
    for i in range(size):
        s = items[i]
        sys.stdout.write(reversedSecondInput[s])
        offset.append(reversedSecondInput[s])
    hexedList.append(offset)
    print("")

print("")
print("--- bin of encrypted code ---")
print("-----------------------------")
print("")

for hexes in hexedList:
    size = len(hexes)
    for i in range(size):
        s = hexes[i][0]
        sys.stdout.write(binMap[s])
        s = hexes[i][1]
        sys.stdout.write(binMap[s])
    print("")
