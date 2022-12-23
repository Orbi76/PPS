
print("Program Started!")
a = str(input("Please enter a standard character:"))

length = len(a)
if length ==1:
    print("The ASCII code for '"+ a + "' is", ord(a))
else:
    print("The input is longer than 1 character")
print("Program Ended!")

print("Program Started!")
b = int(input("Please enter an ASCII code:"))


if b>31 and b<127:
    print("The charachter represented by ASCII code is: "+ chr(b))
else:
    print("The input should be between 32 and 126")
print("Program Ended!")