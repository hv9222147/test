# string :

n = input("enter your first name\n")
print("length of yur name is ",len(n))


# #occurnece of $ in string:
str = ("hi $ i am the $ symbol $98.99")
print(str.count("$"))




# conditional statement :



light = "green"
if(light == "red"):
    print("stop") 
elif(light == "yellow"):
    print("wait")
elif(light == "green"):
     print("go")


#  conditional statement :


age = int(input("enter your age\t\t"))

if(age >= 18):
    print("you can vote")
elif(age <= 18):
    print("you cannot vote")
else:
    print("you cannot vote")



# give a grade depending upon marks:

marks = int(input("enter your marks"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and  marks < 90):
    grade = "B"
elif(marks >=70  and  marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->",grade)

    