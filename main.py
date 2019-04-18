import math

x = int(input("Wanna know what seat will survive? "
              "Enter how many people in the circle: "))

baseof2 = math.log2(x)

if (baseof2 % 1 == 0):
     print("1 is the winning seat")
else:
    factor1 = (math.floor(baseof2))
    factor2 = (x - (2**factor1))
    winning = print(str(2*(factor2) + 1) + (" is the winning seat"))
