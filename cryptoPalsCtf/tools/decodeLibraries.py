# here is the program I wrote to solve cryptopals CTF
# here is my dictionary for convering Base64 digits to 6 bit binary
B64Dict = {
    "000000":"A",
    "000001":"B",
    "000010":"C",
    "000011":"D",
    "000100":"E",
    "000101":"F",
    "000110":"G",
    "000111":"H",
    "001000":"I",
    "001001":"J",
    "001010":"K",
    "001011":"L",
    "001100":"M",
    "001101":"N",
    "001110":"O",
    "001111":"P",
    "010000":"Q",
    "010001":"R",
    "010010":"S",
    "010011":"T",
    "010100":"U",
    "010101":"V",
    "010110":"W",
    "010111":"X",
    "011000":"Y",
    "011001":"Z",
    "011010":"a",
    "011011":"b",
    "011100":"c",
    "011101":"d",
    "011110":"e",
    "011111":"f",
    "100000":"g",
    "100001":"h",
    "100010":"i",
    "100011":"j",
    "100100":"k",
    "100101":"l",
    "100110":"m",
    "100111":"n",
    "101000":"o",
    "101001":"p",
    "101010":"q",
    "101011":"r",
    "101100":"s",
    "101101":"t",
    "101110":"u",
    "101111":"v",
    "110000":"w",
    "110001":"x",
    "110010":"y",
    "110011":"z",
    "110100":"0",
    "110101":"1",
    "110110":"2",
    "110111":"3",
    "111000":"4",
    "111001":"5",
    "111010":"6",
    "111011":"7",
    "111100":"8",
    "111101":"9",
    "111110":"+",
    "111111":"/"

}

# here is a dictionary to convert hex to a four bit digit
hexDict = {
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    "1000":"8",
    "1001":"9",
    "1010":"a",
    "1011":"b",
    "1100":"c",
    "1101":"d",
    "1110":"e",
    "1111":"f"
} 

# I'll also need the inversion of hexDict
invertedHexDict = {value: key for key, value in hexDict.items()}


def convertHexToBinary(someString):
    encodedHex1 = list(someString)
    decodedHex1 = [invertedHexDict[x] for x in encodedHex1]
    return decodedHex1

#for now, take in 8 bits and convert to 2 hex characters
def convertBinaryToHex(someBinary):
    hexOut = list(someBinary)
    hexOut = groupBitsByN(hexOut, 4)
    hexOut = [hexDict[x] for x in hexOut]
    hexOut = "".join(hexOut)
    return hexOut

def groupBitsByN(someList, groupingNumber):
    listToString = "".join(someList)
    groupedList = [listToString[i:i+groupingNumber] for i in range(0, len(listToString), groupingNumber)]
    return groupedList

def encodeSixBitToB64(someList):
    encodedB64 = [B64Dict[x] for x in someList]
    base64Output = "".join(encodedB64)
    return base64Output

def encodeFourBitToHex(someList):
    encodedHex = [hexDict[x] for x in someList]
    xorOutput = "".join(encodedHex)
    return xorOutput

'''def asciiToBinary(someCharacter):
    d = {}
    wb = xlrd.open_workbook('foo.xls')
    sh = wb.sheet_by_index(2)   
    for i in range(138):
        cell_value_class = sh.cell(i,2).value
        cell_value_id = sh.cell(i,0).value
        d[cell_value_class] = cell_value_id'''


    

# take two binary strings and XOR them. Return a string
def xorFunction(firstString, secondString):
    bitString = [None] * len(firstString)
    i = 0
    for bit1, bit2 in zip(firstString, secondString):
        if bit1 == bit2:
            bitString[i] = "0"
            i += 1
        else:
            bitString[i] = "1"
            i += 1
    output = "".join(bitString)
    return output


class B64Encoder:

    myOutput = ""
    
    def __init__(self, var):
        #convert Hex input to binary list
        binaryHexList = convertHexToBinary(var)

        #group into six bit
        sixBitdecodedHex = groupBitsByN(binaryHexList, 6)

        #encode to B64
        sixBitBinaryToB64String = encodeSixBitToB64(sixBitdecodedHex)
        self.myOutput = sixBitBinaryToB64String

    def getOutput(self):
        return self.myOutput


class XorMachine:

    xorOutput = ""
   
    def __init__(self, xor1, xor2):
        # convert Hex inputs to binary lists
        firstBinaryList = convertHexToBinary(xor1)
        secondBinaryList = convertHexToBinary(xor2)

        # convert Lists to strings so we can XOR them
        firstBitString = "".join(firstBinaryList)
        secondBitString = "".join(secondBinaryList)
        
        # do XOR operation
        xorBinaryString = xorFunction(firstBitString, secondBitString)

        # convert output to four bit output
        fourBitList = groupBitsByN(xorBinaryString, 4)

        # encode into Hex
        finalHex = encodeFourBitToHex(fourBitList)
        self.xorOutput = finalHex

    def getOutput(self):
        return self.xorOutput

class xorHexAgainstFile:

    def __init__(self,someHex):
        #convert input to list of 4bit bytes
        binaryHex = convertHexToBinary(someHex)
        binaryHex = groupBitsByN(binaryHex, 8)

        # convert allSingleCharacters.txt to list of 4bit bytes
        hexCharacters = open("allSingleCharacters.txt", "r")
        hexCharacters = hexCharacters.read()
        hexCharacters = hexCharacters.replace(',', '')
        print(hexCharacters)
        hexCharacters = convertHexToBinary(hexCharacters)
        print(hexCharacters)
        hexCharacters = groupBitsByN(hexCharacters, 8)
        print(hexCharacters)

        # XOR each bit in hexCharacters list with the user hex input
        xorFileOut = open("xorFileOut.txt","w+")
        for character in hexCharacters:
            for byte in binaryHex:
                byte1 = groupBitsByN(byte, 4)
                byte1 = [hexDict[x] for x in byte1]
                byte1 = "".join(byte1)
                character1 = groupBitsByN(character, 4)
                character1 = [hexDict[x] for x in character1]
                character1 = "".join(character1)
                #character1 = hexDict[character]
                eachOutput = XorMachine(byte1, character1)
                xorFileOut.write(eachOutput.getOutput())
            xorFileOut.write("\n")
        xorFileOut.close()