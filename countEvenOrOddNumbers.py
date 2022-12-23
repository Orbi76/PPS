firstNumber = int(input("Please give the first number!"))
secondNumber = int(input("Please give the second number!"))
thirdNumber = int(input("Please give the third number!"))
totalOdd = 0
totalEven = 0
if firstNumber%2 == 0:
    totalEven = totalEven+1
else: totalOdd = totalOdd+1
if secondNumber%2 == 0:
    totalEven = totalEven+1
else: totalOdd = totalOdd+1
if thirdNumber%2 == 0:
    totalEven += 1
else: totalOdd += 1
print("There were "+str(totalEven)+" even and "+str(totalOdd)+" odd numbers")

