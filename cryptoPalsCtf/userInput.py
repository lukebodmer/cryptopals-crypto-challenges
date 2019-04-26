from tools.decodeLibraries import base64encoder 
from tools.decodeLibraries import xorMachine
from tools.decodeLibraries import xorHexAgainstFile
from tools.decodeLibraries import convertHexToBytes
from tools.scoringPlainText import compareDecodedWithEnglish
from tools.decodeLibraries import findKey
import binascii

class Error(Exception):
   """Base class for other exceptions"""
   pass

class PickARealOptionError(Error):
    '''Raised when User is a noob and can't pick from a list'''
    pass

class TypeRealHexError(Error):
    '''Raised when User is a noob and can't type hex'''
    pass

class ExitProgram(Error):
    '''Given to abort cmd at various times'''
    pass

def grabHexFromUser(var):

    userHex = []

    if var == '1':
        userHex.append(input("\n Enter the Hex you would like to convert to Base64:  "))
    elif var == '2':
        userHex.append(input("\n Enter the first hex value to XOR:  "))
        userHex.append(input("\n Enter the second hex value to XOR:  "))
    elif var == '3':
        userHex.append(input("\nEnter the Hex you would like to decode:  "))
    return userHex


def makeSureItsHex(var):
    globalHexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    while True:
        try:
            grabHex = grabHexFromUser(var)
            for eachHex in grabHex:
                if eachHex == 'exit':
                    raise ExitProgram
                else:
                    for eachHex in grabHex:
                        checkHex = list(eachHex)
                        for x in checkHex:
                            if x in globalHexList:
                                pass
                            else:
                                raise TypeRealHexError
            return grabHex
        except TypeRealHexError:
            print("\n >>>That doesn't seem to be hex. Please try again<<<")
            
            
# make sure the user picks an avaliable option
def pickATask():
    while True:
        try:
            var = input("\nWhat would you like to do?:\n \
                1) Convert Hex to Base 64\n \
                2) XOR two equal length Hex strings\n \
                3) Decode a string that has been XOR'd with a character\n \
                4) exit\n\n")
            optionList = ['1', '2', '3', '4']
            if var in optionList:
                return var
            elif var == '4':
                raise ExitProgram
            elif var == 'exit':
                raise ExitProgram
            else:
                raise PickARealOptionError
        except PickARealOptionError:
            print("Please type the number of the option you want")



def collectUserInput(userIn):
    if userIn == "1":
        hexNumber = makeSureItsHex(userIn)
        hexNumber = "".join(hexNumber)
        hexBinaryArray = convertHexToBytes(hexNumber)
        answer = base64encoder(hexBinaryArray)
        print("\nThe encoded B64 output is: ", answer)
    elif userIn == "2": 
        xor = makeSureItsHex(userIn)
        xor1 = convertHexToBytes(xor[0])
        xor2 = convertHexToBytes(xor[1])
        print("\nXOR'd output is:", xorMachine(xor1,xor2))
    elif userIn == '3':
        hexNumber = makeSureItsHex(userIn)
        hexNumber = "".join(hexNumber)
        hexBinaryArray = convertHexToBytes(hexNumber)
        xorHexAgainstFile(hexBinaryArray)
        findKey()
    else:
        print("How did you get here?")


def startProgram():
    while True:
        try:
            userValue = pickATask()
            collectUserInput(userValue)
        except ExitProgram:
            print("Bye!")
            break
