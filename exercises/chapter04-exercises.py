# chapter 4
# functions

# random number program
import random
for i in range(10):
    x = random.random()
    print(x)

# lyric program
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# def - indicates the start of a function & that the following indented section of code is to be stored for later

def fred():
    print("Zap")

def jane():
    print("ABC")

jane() # ABC
fred() # Zap
jane() # ABC

# pay program
hours = input('Enter Hours:\n')
rate = input('Enter Rate:\n')
try:
    hrs = float(hours)
    rt = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
def computepay(hours, rate):
    if hrs <= 40.0:
        pay = hrs * rt
    else:
        regpay = 40.0 * rt
        otpay = (hrs - 40.0) * (rt * 1.5)
        pay = regpay + otpay
    return pay
print('Pay:')
print(computepay(hours, rate))

# grade program
score = input('Enter Score:\n')
try:
    grade = float(score)
except:
    print('Bad score')
    quit()
def computegrade(score):
    if grade >= 0.9 and grade <= 1.0:
        score = 'A'
    elif grade >= 0.8 and grade < 0.9:
        score = 'B'
    elif grade >= 0.7 and grade < 0.8:
        score = 'C'
    elif grade >= 0.6 and grade < 0.7:
        score = 'D'
    elif grade >= 0.0 and grade < 0.6:
        score = 'F'
    else:
        score = 'Out of range'
    return score
print(computegrade(score))
