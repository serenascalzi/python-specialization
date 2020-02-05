# chapter 8
# lists

# chop/middle function
def middle(t):
    end = len(t) - 1
    return t[1:end]

alpha = ['a', 'b', 'c', 'd', 'e']
mid = middle(alpha)
print(mid)

# dow program
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])

# romeo program
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
allwords = list()
for line in fhand:
    words = line.split()
    for word in words:
        if not word in allwords:
            allwords.append(word)
allwords.sort()
print(allwords)

# from program
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')

# numbers program
numbers = list()
while True:
    number = input('Enter a number:\n')
    if number == 'done':
        break
    try:
        num = float(number)
    except:
        print('Invalid input')
        continue
    numbers.append(number)
maximum = float(max(numbers))
minimum = float(min(numbers))
print('Maximum:', maximum)
print('Minimum:', minimum)
