# Program to prompt the user to enter a list of numbers and then print the
# numbers with any duplicates removed

# Prompt for list of numbers
number_list=[]
num = int(input('Enter a number, 0 to quit'))
while num != 0:
    number_list.append(num)
    num = int(input('Enter a number, 0 to quit'))
# Create new list and add numbers to it but only if they’re not already in the list
unique_list=[]
for x in number_list:
    if x not in unique_list:
        unique_list.append(x)

# Print list with duplicates removed
print('List after removing duplicates is…')
print(unique_list)
