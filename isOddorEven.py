"""This file is for defining 3 functions,
isOdd, returns true if odd, isEven, returns,
true if even, and isOddorEven, which will
tell you if something is odd or even."""

def isOdd(number):
    if(isinstance(number, float)):
        return False
    elif(number%2) != 0:
        return True
    else: return False

    
def isEven(number):
    if(isinstance(number, float)):
        return False
    elif(number%2) == 0:
        return True
    else: return False

def isOddorEven(number):
    if(isinstance(number, float)):
        print("That's a decimal, guy.")
    elif(number%2) == 0:
        print("The " + str(number) + " is even.")
    else:
        print("The " + str(number) + " is odd.")




assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
isOddorEven(43)
isOddorEven(-43)
isOddorEven(42)
isOddorEven(-42)
isOddorEven(3.1415)
isOddorEven(-3.1415)
