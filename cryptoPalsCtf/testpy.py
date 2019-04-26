import binascii
import codecs
import math


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

f = open("prideAndPrejudice.txt",encoding="utf8")
string = f.read()

fo = open("xorFileOut.txt", "r")
line = fo.readline()


a = scorePlainText(string)
a = normalizeKeyValues(a)
b = scorePlainText(line)
b = normalizeKeyValues(b)

c = compareCharcterFreq(a, b)
print(a)
print(b)
print(c)