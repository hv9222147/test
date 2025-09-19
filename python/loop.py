#sum of even number:



# n = int(input("enter your number: \t"))
# sum_even  = 0

# for i in range (0,n+1):
#     if i%2 ==0:
#         sum_even +=1
# print("sum of even number is :",sum_even)



#multiplication of number :


# n = int(input("enter your number: \t"))


# for i in range(1,11):
#     if i ==5:
#         continue
#     print(n,"x", i ,'=',n*i)

# for i in range(1,11):
#     if i ==5:
#         continue
#     print(n*i)


#repeat char:

# str = "gghyyhuuuygds"

# for char in str:
#     print(char)
#     if str .count(char) == 1:
#         print("char is :", char)
#         break


#factorial of number:

# n = int(input("enter a number:  \t"))
# factorial = 1

# while n > 0:
#     factorial *= n
#     n -= 1
# print("factorial is:",factorial)


#take a inout from user no to 1 to 10:

# while True:
#     n = int(input("enter a number for 1 to 10: \t"))



#     if (1 <= n <= 10):
#         print("thanks")
#         break
#     else:
#         print("invalid pls try agian")

# prime number checker:


# n = int(input("enter a no. is: "))

# prime = True

# if n > 1:
#     for i in range(2,n):
#         if (n % i) ==0:
#             prime = False
#             break
# print(prime)

#check the item is duolicate or not :

items = ["apple","banana","orange","mango","apple","mango","orange"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate",item)
       
    else:
     unique_item.add(item)


# items = ["apple","banana","orange","mango","apple","mango","orange"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("duplicate:", item)
#     else:
#         unique_item.add(item)