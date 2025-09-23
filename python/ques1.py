

# #operators:

# if(num1 == 1 or num1 == 11)and num2 == 10:
#     print("it is perfect combination")
# else:
#     print("loose")



# if (num1 == 1 or num1 == 11) and num2 == 10:
#     print("Perfect combination!")
# else:
#     print("You lose!")


# x = 7
# y = 2
# z = x>3 and y<1



#question1 for python in function:

# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#         return sum(args)
# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5,6,7))


#question 2 for python in function:

# def kwargs(**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#      print(f"{key} : {value}")
#     return kwargs
# print(kwargs(name ="harsh verma",age=21,city="Bhiwani"))

#question 3 for python in function:

# def greet(name = "HARSH"):
#     return "hello " + name +"!"
# print(greet("VERMA"))



#question 4 for python in function:

# def is_even(num):
#     if num% 2 ==0:
#         return True
#     else:
#         return False
# num = int(input("enter a number: "))
# result = is_even(num)
# print("the number is even: ",result)



#question 5 for python in function:

# import math

# def circle(radius):
#     area =math.pi*radius**2
#     return area

# a = circle(5)
# print("area is :", round(a,2))

#question 6 for python in function:

# def max_of_two(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# a = float(input("enter first number: "))
# b = float(input("enter second number: "))
# result = max_of_two(a,b)
# print("the max number is: ",result)


# question 7 factorial number ,function:

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("enter anumber: "))
result = factorial(n)
print("factorial is :",result)
   
    