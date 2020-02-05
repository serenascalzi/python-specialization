# chapter 10
# tuples

# from email program
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
allwords = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        allwords.append(words[1])
email = dict()
for word in allwords:
    if word not in email:
        email[word] = 1
    else:
        email[word] += 1
dsort = list()
for key, val in list(email.items()):
    dsort.append((val, key))
dsort.sort(reverse = True)
for key, val in dsort[:1]:
    print(val, key)

# from hod program
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
allwords = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        allwords.append(words[5])
hrwords = list()
for word in allwords:
    index = word.find(':')
    hrwords.append(word[:index])
hours = dict()
for word in hrwords:
    if word not in hours:
        hours[word] = 1
    else:
        hours[word] += 1
hsort = list()
for key, val in list(hours.items()):
    hsort.append((key, val))
hsort.sort(reverse = False)
for key, val in hsort:
    print(key, val)

# letter program
import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
allletters = list()
for line in fhand:
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', '0123456789'))
    words = line.split()
    for word in words:
        letters = tuple(word)
        for letter in letters:
            allletters.append(letter)
fletters = dict()
for letter in allletters:
    if letter not in fletters:
        fletters[letter] = 1
    else:
        fletters[letter] += 1
lsort = list()
for key, val in list(fletters.items()):
    lsort.append((val, key))
lsort.sort(reverse = True)
for key, val in lsort:
    print(val, key)
