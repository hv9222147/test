
# # task 1: calculator;


# def calculator(a, b, op):
#     if op == "1" or op == '+':
#         return a + b
#     elif op == "2" or op == '-':
#         return a-b
#     elif op =="3" or op =='*':
#         return a*b
#     elif op =="4" or op == '/':
#         if b!=0:
#             return a/b
#         else:
#             return "not division by zero"
#     elif op =="5" or op == '%':
#         return a%b
#     else:
#         return "invalid input"
# print("select your operation from below:")
# print("1.addition(+)")
# print("2.subtraction(-)")
# print("3.multipliation(*)")
# print("4.division(/)")
# print("5.modulus(%)")
# a = float(input("enter first number: "))
# b = float(input("enter second number: "))
# op = input("enter your  operator(1/2/3/4/5): ")
# result = calculator(a,b,op)
# print("the result is: ",result)


# task 2:  prime no. upto a limit :




# def prime_number(n):
#     if n <= 1:
#         return "it is not a prime number"
#     for i in range(2, n):
#             if n % i == 0:
#                 return "it is not a prime number"
#     return "it is a prime number"
# n =  int(input("enter a number: "))
# result = prime_number(n)
# print("the number is :",result)



# def prime_upto(limit):
#     prime = []
#     for num in range(2,limit + 1):
#         is_prime = True
#         if num >1:
#             for i  in range(2,int(num**0.5)+1):
#                 if num % i == 0:
#                     is_prime = False
#                 break
#         if is_prime:
#             prime.append(num)
#     return prime


# limit  = int(input("enter a limit: "))
# result = prime_upto(limit)
# print("prime number upto limit is:",result)



# task 3: unique element is list without using set():

# def unique_elements(list):
#     unique = []
#     for item in list:
#         if item not in unique:
#             unique.append(item)
#     return unique

# list =[1,2,3,4,5,1,2,3]
# result = unique_elements(list)
# print("the unique elements is list is:",result)


# task 4 : word count :

# def word_count(sentence):
#     word_count = {}
#     words = sentence.split()
#     for word in words:
#         word = word.lower()
#         if word in word_count:
#             word_count[word] +=1
#         else:
#             word_count[word]=1
#     return word_count
# sentence = input("enter a sentence: ")
# result = word_count(sentence)
# print("the  word count is: ",result)


# task 5:




# def palindrome(string):
#     string = string.lower()
#     reversed_string = string[:: -1]
#     if string == reversed_string:
#         return True
#     else:
#         return False
# string = input("enter a string: ")
# result = palindrome(string)
# print("the string is palindrome:",result)


# task 6;

def car(brand,model):
    return f"car brand is {brand} \n and mode is {model}"
result = car("BMW","X7")
print(result)
