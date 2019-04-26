

def listOfAscii():
    '''returns a list of all Ascii characters'''
    asciiChars = range(32,126)
    testText = []
    for i in asciiChars:
        testText.append(chr(i))
    return testText


def scorePlainText(plainText):
    '''returns a dictionary of character frequency of Ascii characters in a text'''
    charFreq = {} 
    asciiList = listOfAscii()

    for i in plainText: 
        if i in asciiList: 
            if i in charFreq:
                charFreq[i] += 1
            else:
                charFreq[i] = 1
        else: 
            pass
    return charFreq


def normalizeKeyValues(someDict):
    factor=1.0/sum(someDict.values())
    for k in someDict:
        someDict[k] = someDict[k]*factor
    return someDict

def compareCharcterFreq(testTextDict, decodedStringsDict):

    sumOfDiferences = 0

    for x in testTextDict:
        if x in decodedStringsDict:
            tempSum = abs(testTextDict[x] - decodedStringsDict[x])
            sumOfDiferences = sumOfDiferences + tempSum
        else:
            pass
    return sumOfDiferences

def compareDecodedWithEnglish(decodedStringFile):

    f = open("prideAndPrejudice.txt",encoding="utf8")
    englishExample = f.read()
    testText = scorePlainText(englishExample)
    testText = normalizeKeyValues(testText)

    decodedKey = open(decodedStringFile, "r")

    scorelist = []

    for line in decodedKey:
        line = line[11:]
        codeCharacters = scorePlainText(line)
        codeCharacters = normalizeKeyValues(codeCharacters)
        score = compareCharcterFreq(testText, codeCharacters)
        scorelist.append(score)
    
    decodedKey.close()
    f.close()
    
    return scorelist.index(min(scorelist))


