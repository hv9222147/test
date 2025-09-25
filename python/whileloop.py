timer= 1
while timer <=5:
    print(timer)



# Star triangle pattern
rows = int(input("enter a row"))

for i in range(1, rows + 1):
    print("*" * i)




minute = 5

while minute > 0:
    print(minute)
    second = 60
    while second > 0:
        if second % 10 == 0:
            print(second) 
        second = second - 1

    if minute == 2:
        print("Almost there!")
        
        
        minute = minute - 1

print("Time's up!!")





	

minute = 5

while minute > 0:
    print(minute)
    second = 60
    while second > 0:
        if second % 10 == 0:
            print(second) 
        second = second - 1

    if minute == 2:
        print("Almost there!")

    minute = minute - 1

print("Time's up!!")





import random

random.seed(70053)

x = 9999
while x > 0:
    x = random.random()
    print(x)


import math

n = float(input("Please enter a number: "))

# Your code...
# ... computes the square root ...
# and stores it in a variable called "estimate" 

gold_reference = math.sqrt(n)
if abs(estimate - gold_reference) < 0.00001:
    print("Correct answer.")
else:
    print(f"Incorrect. Program output is {estimate}, but I am expecting {gold_reference}.")
