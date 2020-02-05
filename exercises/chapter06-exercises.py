# chapter 6
# strings

# traversal program
word = input('Enter Word:\n')
index = len(word) - 1
while index >= 0:
    letter = word[index]
    print(letter)
    index = index - 1

# fruit[:] - means a slice starting at the beginning and going to the end of the string

# count program
word = input('Enter Word:\n')
letter = input('Enter Letter:\n')
def count(word, letter):
    total = 0
    for char in word:
        if char == letter:
            total = total + 1
    return total
print(count(word, letter))

# string methods
word = 'banana'
print(word.count('a'))

str = 'X-DSPAM-Confidence:0.8475'
start = str.find(':')
number = str[start+1:]
num = float(number)
print(num)
