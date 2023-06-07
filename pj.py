import random

count = 0
x = 1
while x != 10:
    x = random.randint(0,11)
    count += 1

print(count)
#just adding comment
y = input('Please introduce yourself: ')
def intro(x):
    print(f'Here is your introduction: {x}')

intro(y)
