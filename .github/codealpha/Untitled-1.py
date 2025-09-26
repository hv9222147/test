
# question 1:



# def loop(num):
#     for i in range(1,num+1):
#         print(i)
#     return num

# num = int(input("enter a number:"))
# result = loop(num)
# print("the number is:",result)


#question 2:

# def multiplication(n):
#     for i in range(1,11):
#         print(n,"x",i,"=",n*i)
#     return n
# n = int(input("enter a number: "))
# result =  multiplication(n)
# print("the number is:",result)

# question 3:

def calculate_sum(n):
    total = 0
    for i in range(1,n+1):
        total +=i
    return total
   
   
num = int(input("enter a number:"))
result = calculate_sum(num)
print("the sum is:",result)
