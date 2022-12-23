print('Calculate the BMI index!')
name = input('What is your name?')
age = float(input('How old are you /(in years/)?'))
hig = float(input('How tall are you /(in meters/)?'))
weight = float(input('How much do you weight /(in kilograms/)?'))
value = weight/hig ** 2
print(f'{name} you are {age:0} years old and your bmi is  {value:2}')
print(f'Your BMI is {value:3}')
