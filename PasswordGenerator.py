#Import random module
from random import *

#Global-asking
level = 0
llist = 0

#Simbols
levone = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
levtwo = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
levtwo += levone
levthree = ["", "#", "-", "^", "$", "*"]
levthree += levtwo

#Generate password
def Gen(level):
    tipe = int(input("Select the number of characters: "))
    if level == 1:
        llist = [choice(levone) for i in range(tipe)]
    elif level == 2:
        llist = [choice(levtwo) for i in range(tipe)]
    elif level == 3:
        llist = [choice(levthree) for i in range(tipe)]
    print(llist)
    string = ''.join(str(i) for i in llist)
    print(string)

#SETUP-PART
def Setup():
    #Setup part 1
    def Sone():
        print ("Select password level:")
        print("1.Easy (Only numbers)")
        print("2.Medium (Numbers and letters)")
        print("3.Hard (Numbers, letters and special)")
        tipe = int(input("Your choose: "))
        Gen(tipe)
        if tipe == 1:
            print("> Hm... Okay..?")
            level = 1
        elif tipe == 2:
            print(">> Good")
            level = 2
        elif tipe == 3:
            print(">>> VERY GOOD")
            level = 3
        else:
            print("ERROR: Rebooting...")
            print("---------------------------------")
            Sone()
        print("Generate > Gen()")

    #Start setup
    Sone()


Setup()