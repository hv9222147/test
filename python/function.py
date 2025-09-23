# question 1 for python in function:


# def square(number):
#     print(number**3)
#     return number**3

    

# result = square(4)
# print(result)


#question 2 for python in function:

# def add(a,b):
#     return a+b


# print(add(10,14))

#  question 3 for python in function:

# def multiply(p1,p2):
#     return p1 * p2

# print(multiply(4,5))
# print(multiply("H",5))
# print(multiply(4,"V"))

# question 4 for python in function:

# import math

# def circle(radius):
#     area = math.pi*radius**2
#     circumference = 2*math.pi*radius
#     return area,circumference

# a,c = circle(5)
# print("area is: ",round(a,2),"\n","circumference is :",round(c,2))


#question 5 for python in function:

# def add(name = "HARSH"):
#     return "hello " +name +"!"

# print(add("VERMA"))


# question 6 for python in function:

# cube = lambda x, y: (x**3, y**3)

# result = cube(2,3)
# print("cube of x is :",result[0])
# print("cube of y is:",result[1])


# question 7  for python in function:




# def check_number(num):
#     if num>0:
#         return "positive"
#     elif num <0:
#         return "negative"
#     else:
#         return "zero"
    


# num = int(input("enter a number: "))
# result = check_number(num)
# print("the number is",result)

#question 8 for python in function:

# def check_divisible(num):
#     if num %5==0 and num %3==0:
#         return True
#     else:
#         return False

# num = int(input("enter a number: "))
# result = check_divisible(num)
# print("the number is divisible by 5 and 11 is:",result)

# question 9 for python in function:

# def max_of_three(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))
# result = max_of_three(a,b,c)
# print("the number is max: ",result)

#question 10 for python in function:

def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
marks = float(input("enter your marks(int or decimal): "))
result = check_pass_fail(marks)
print("you are :",result)
