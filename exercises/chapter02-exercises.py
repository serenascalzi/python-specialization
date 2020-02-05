# chapter 2
# variables, expressions, and statements

5
x = 5
x + 1 # 6

# welcome program
name = input('Enter your name:\n')
print('Hello ', name)

# pay program
hours = input('Enter Hours:\n')
rate = input('Enter Rate:\n')
pay = float(hours) * float(rate)
print('Pay:', pay)

# expression values/types
width = 17
height = 12.0
width // 2 # 8, int
width / 2.0 # 8.5, float
height / 3 # 4, float
1 + 2 * 5 # 11, int

# temperature program
tempC = input('Enter Celsius Temperature:\n')
tempF = (float(tempC) * 9.0 / 5.0) + 32.0
print('Fahrenheit Temperature:', tempF)
