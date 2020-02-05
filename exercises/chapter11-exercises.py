# chapter 11
# regular expressions

# grep program
import re
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
regexp = input('Enter a regular expression: ')
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(regexp, line):
        count = count + 1
print(fname, 'had', count, 'lines that matched', regexp)

# new revision program
import re
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    number = re.findall('^New Revision: ([0-9]+)', line)
    if len(number) > 0:
        num = float(number[0])
        total = total + num
        count = count + 1
average = total / count
print(average)

# graded external tool
import re
fhand = open('regex_sum_198089.txt')
sum = 0
for line in fhand:
    numbers = re.findall('([0-9]+)', line)
    if len(numbers) > 0:
        for number in numbers:
            num = int(number)
            sum = sum + num
print(sum)

# just for fun
# Python 3
# import re
# print(sum([****** *** * in **********('[0-9]+',**************************.read())]))
