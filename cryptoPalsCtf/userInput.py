from tools.decodeLibraries import B64Encoder 
from tools.decodeLibraries import XorMachine
from tools.decodeLibraries import convertHexToBinary
from tools.decodeLibraries import xorHexAgainstFile

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

def makeSureItsHex(someHex):
    globalHexList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    try:
        if someHex == 'exit':
            raise ExitProgram
        userList = list(someHex)
        for x in userList:
            if x in globalHexList:
                pass
            else:
                raise TypeRealHexError
        return someHex
    except TypeRealHexError:
        raise TypeRealHexError

#takes in a string of Hex, makes sure its legit, and returns the same string
def takeInHex(var):
    while True:    
        if var == '1':
            try: 
                userHex = input("\n Enter the Hex you would like to convert to Base64:  ")
                reasonableHex = makeSureItsHex(userHex)
                return reasonableHex
            except TypeRealHexError:
                print("\n >>>That doesn't seem to be hex. Please try again<<<")
        elif var == '2':
            while True:
                try:
                    userHex1 = input("\n Enter the first hex value to XOR:  ")
                    reasonableHex1 = makeSureItsHex(userHex1)
                    break
                except TypeRealHexError:
                    print("\n >>>That doesn't seem to be hex. Please try again<<<")
            while True:
                try:
                    userHex2 = input("\n Enter the second hex value to XOR:  ")
                    reasonableHex2 = makeSureItsHex(userHex2)
                    return reasonableHex1, reasonableHex2
                except TypeRealHexError:
                    print("\n >>>That doesn't seem to be hex. Please try again<<<")
        elif var == '3':
            while True:
                try: 
                    userHex = input("\n Enter the Hex you would like to convert to binary:  ")
                    reasonableHex = makeSureItsHex(userHex)
                    return reasonableHex
                except TypeRealHexError:
                    print("\n >>>That doesn't seem to be hex. Please try again<<<")
        elif var == '4':
            while True:
                try:
                    userHex = input("\n Enter the Hex you would like to XOR against single characters:  ")
                    reasonableHex = makeSureItsHex(userHex)
                    return reasonableHex
                except TypeRealHexError:
                    print("\n >>>That doesn't seem to be hex. Please try again<<<")
        

            

def pickATask():
    while True:
        try:
            var = input("\nWhat would you like to do?:\n \
                1) Convert Hex to Base 64\n \
                2) XOR two equal length Hex strings\n \
                3) decode a hex string to binary\n \
                4) XOR a hex string against every single character\n \
                5) exit\n\n")
            optionList = ['1', '2', '3', '4']
            if var in optionList:
                return var
            elif var == '5':
                raise ExitProgram
            elif var == 'exit':
                raise ExitProgram
            else:
                raise PickARealOptionError
        except PickARealOptionError:
            print("Please type the number of the option you want")



def collectUserInput(userIn):
    if userIn == "1":
        hexNumber = takeInHex(userIn)
        answer = B64Encoder(hexNumber)
        print("\nThe encoded B64 output is: ", answer.getOutput())
    elif userIn == "2": 
        xor1, xor2 = takeInHex(userIn)
        print("\nXOR'd output is:", XorMachine(xor1,xor2).getOutput())
    elif userIn == "3":
        hexNumber = takeInHex(userIn)
        binaryList = convertHexToBinary(hexNumber)
        binaryOut = "".join(binaryList)
        print("\nThe decoded binary is:", binaryOut)
    elif userIn == '4':
        hexNumber = takeInHex(userIn)
        xorHexAgainstFile(hexNumber)
        '''f = open('')
        file_contents = f.read()
        print (file_contents)
        f.close'''
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
