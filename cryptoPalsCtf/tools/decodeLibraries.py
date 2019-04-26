import codecs
import binascii
from tools.scoringPlainText import compareDecodedWithEnglish
# here is the program I wrote to solve cryptopals CTF
# here is my dictionary for convering Base64 digits to 6 bit binary

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

def findKey():
    bestScore = compareDecodedWithEnglish("xorFileOut.txt")
    print(bestScore)
    xorFileOut = open("xorFileOut.txt","r")
    bestScoreLine = xorFileOut.read().split('\n')[bestScore]
    print("\n Your decoded Key is:   ", bestScoreLine[12:-2])
