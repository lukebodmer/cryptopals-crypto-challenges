#this is a function that converts Hex to Base64

from userInput import dealWithUserInput
from tools.decodeLibraries import B64Encoder 
from tools.decodeLibraries import XorMachine

if __name__ == "__main__":
    dealWithUserInput()
'''if __name__ == "__main__":
    while True:
        var = input("\nWhat would you like to do?:\n 1) Convert Hex to Base 64\n 2) XOR two equal length Hex strings\n 3) exit\n\n")
        if var == "1":
            hexNumber = input("\n Enter the Hex you would like to convert to Base64:  ")
            answer = B64Encoder(hexNumber)
            print("\nThe encoded B64 output is: ", answer.getOutput())
        elif var == "2": 
            xor1 = input("\n Enter the first hex value to XOR:  ")
            xor2 = input("\n Enter the second hex value to XOR:  ")
            print("\nXOR'd output is:", XorMachine(xor1,xor2).getOutput())
        elif var == "exit":
            break
        elif var == "3":
            break
        else:
            print ("\n Sorry I don't recognize that input. Try again")'''
