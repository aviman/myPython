#Program to divide for given Dividend and Divisor

import sys

try:
    dividendNumber = float(input("Enter the Dividend : "))
    divisorNumber = float(input("What will be the Divisor : "))


    quotientResult = dividendNumber/divisorNumber

except ZeroDivisionError:
    print("Divisor cannot be 0")


except:
    error = sys.exc_info()[0]
    print(error)

else:
    print("Result of Division is {}".format(quotientResult))
    


                       
