# chapter 9
# dictionaries

# dictionary program
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
allwords = list()
pywords = dict()
count = 0
for line in fhand:
    words = line.split()
    for word in words:
        if not word in allwords:
            allwords.append(word)
            pywords[count] = word
            count = count + 1
print(pywords)

# search function
def search(wd):
    lookup = list(pywords.values())
    return wd in lookup

term = 'creative'
tm = search(term)
print(tm)

# from dow program
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
        allwords.append(words[2])
dow = dict()
for word in allwords:
    if word not in dow:
        dow[word] = 1
    else:
        dow[word] += 1
print(dow)

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
largest = None
for key in email:
    if largest is None or email[key] > largest:
        maximum = key
        largest = email[key]
print(maximum, largest)

# from domain program
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
domwords = list()
for word in allwords:
    index = word.find('@')
    domwords.append(word[index + 1:])
domain = dict()
for word in domwords:
    if word not in domain:
        domain[word] = 1
    else:
        domain[word] += 1
print(domain)
