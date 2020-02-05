# chapter 3
# conditional execution

# pay program
hours = input('Enter Hours:\n')
rate = input('Enter Rate:\n')
try:
    hrs = float(hours)
    rt = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
if hrs <= 40.0:
    pay = hrs * rt
else:
    regpay = 40.0 * rt
    otpay = (hrs - 40.0) * (rt * 1.5)
    pay = regpay + otpay
print('Pay:', pay)

# grade program
score = input('Enter Score:\n')
try:
    grade = float(score)
except:
    print('Bad score')
    quit()
if grade >= 0.9 and grade <= 1.0:
    print('A')
elif grade >= 0.8 and grade < 0.9:
    print('B')
elif grade >= 0.7 and grade < 0.8:
    print('C')
elif grade >= 0.6 and grade < 0.7:
    print('D')
elif grade >= 0.0 and grade < 0.6:
    print('F')
else:
    print('Out of range')
