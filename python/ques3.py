# n = int(input("Enter a number: "))
# is_prime = True

# if n <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(n, "is a Prime number")
# else:
#     print(n, "is not a Prime number")
    
import math 
sigmoid = 1/(1+math.exp(0.6))
print(sigmoid)