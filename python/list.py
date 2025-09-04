#list question :



movies=[]
mov1 = input(" enter your 1st movie")
movies.append(mov1)
mov2 = input("enter your 2nd movies")
movies.append(mov2)
mov3 = input("enter your 3rd movies")
movies.append(mov3)


print(movies)

# list palindrome question :

list1 = [1,2,1]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("IT IS A PALINROME")
else:
    print("IT IS NOT A PALINDROME")
