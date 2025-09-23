

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

def kwargs(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
     print(f"{key} : {value}")
    return kwargs
print(kwargs(name ="harsh verma",age=21,city="Bhiwani"))
