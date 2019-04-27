import codecs
import binascii
import userInput
import math
from tools.scoringPlainText import compareDecodedWithEnglish
# here is the program I wrote to solve cryptopals CTF
# here is my dictionary for convering Base64 digits to 6 bit binary
class Error(Exception):
   """Base class for other exceptions"""
   pass

class badHexFile(Error):
    '''Given when the file decodedStringData is no good'''
    pass

def convertBytesToHex(bytesArray):
    hexData = binascii.hexlify(bytesArray)
    return hexData

def convertHexToBytes(hexString):
    userBytes = bytearray(binascii.unhexlify(hexString))
    return userBytes

def base64encoder(userByteArray):
        # convert userByteArray to B64 input to binary list
        encodedB64 = binascii.b2a_base64(userByteArray)
        return encodedB64

def xorMachine(userBytes1, userBytes2):
    '''recieves two byte objects and XORs them''' 
    xorResult = bytearray()
    for bytes1, bytes2  in zip(userBytes1, userBytes2):
        xorResult.append(bytes1 ^ bytes2)
    hexData = binascii.hexlify(xorResult)
    return hexData

def singleXorMachine(userBytes1, userBytes2):
    xorResult = bytearray()
    xorResult.append(userBytes1 ^ userBytes2)
    return xorResult 

def xorHexAgainstFile(userBytes):

    xorFileOut = open("xorFileOut.txt","w+")
    asciiByteList = bytes(range(32,126))
    xorByteArray = bytearray()

    for asciiByte in asciiByteList:
        for byte in userBytes:
            eachOutput = singleXorMachine(byte, asciiByte)
            xorByteArray.append(int.from_bytes(eachOutput, byteorder='big'))
        xorFileOut.write(str(xorByteArray))
        xorFileOut.write("\n")
        xorByteArray = bytearray()
    xorFileOut.close()

def findKey(val):
    bestScore = compareDecodedWithEnglish("xorFileOut.txt")
    bestEncodedKeyScore = bestScore/94
    bestEncodedKeyScore = math.ceil(bestEncodedKeyScore)
    fileLine = bestEncodedKeyScore - 1
    xorFileOut = open("xorFileOut.txt","r")
    keyFile = open("decodedStringData.txt", "r")
    bestScoreLine = xorFileOut.read().split('\n')[bestScore]
    bestScoreEncodedLine = keyFile.read().split('\n')[fileLine]
    print("\n Your decoded Key is:   ", bestScoreLine[12:-4])
    if val == '1':
        print(" the accompanying encoded Key is:   ", bestScoreEncodedLine)
        print(" the position of the key in the file is line", bestEncodedKeyScore)
    xorFileOut.close()
    keyFile.close()

def detectSingleCharacterXor():
    #read first line of decodedStringData, XOR against all single characters and store in a file
    #repeat for all lines of the file
    xorFileOut = open("xorFileOut.txt","w+")
    keyFile = open("decodedStringData.txt", "r")
    asciiByteList = bytes(range(32,126))
    xorByteArray = bytearray()
    try:
        for key in keyFile:
            hexNumber = userInput.makeSureItsHex('fix this shitty code',key)
            hexBinaryArray = convertHexToBytes(hexNumber)
            for asciiByte in asciiByteList:
                for byte in hexBinaryArray:
                    eachOutput = singleXorMachine(byte, asciiByte)
                    xorByteArray.append(int.from_bytes(eachOutput, byteorder='big'))
                xorFileOut.write(str(xorByteArray))
                xorFileOut.write("\n")
                xorByteArray = bytearray()
        xorFileOut.close()
        findKey('1')
    except badHexFile:
        print("\n >>>There is a problem with your Hex file. Abort!<<<")