#Program to check if Input Number is Prime or Composite

import sys

try:
    inputNumber = int(input("Enter any number : "))
    if inputNumber ==0 or inputNumber == 1:
        raise ValueError(inputNumber)
except ValueError:
    print("Please enter a number other then 0 and 1")
except:
    print("Not a valid number")
else:
    counterNumber = 2
    while counterNumber< inputNumber:
        isComposite = inputNumber%counterNumber
        if isComposite == 0:
            print("{} is a Composite Number".format(inputNumber))
            break
        counterNumber += 1
    if counterNumber == inputNumber:
        print("{} is a Prime Number".format(inputNumber))

finally:
    print("Are you Satisfied!!")
