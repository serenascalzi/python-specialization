# chapter 5
# iteration

# numbers average program
total = 0
count = 0
while True:
    number = input('Enter a number:\n')
    if number == 'done':
        break
    try:
        num = int(number)
    except:
        print('Invalid input')
        continue
    total = total + num
    count = count + 1
average = total / count
print(total, count, average)

# numbers outliers program
total = 0
count = 0
largest = None
smallest = None
while True:
    number = input('Enter a number:\n')
    if number == 'done':
        break
    try:
        num = int(number)
    except:
        print('Invalid input')
        continue
    total = total + num
    count = count + 1
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
print(total, count, largest, smallest)
