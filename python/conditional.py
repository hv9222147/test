 # CLASSIFY A PERSON'S AGE GROUP :
 

# age = int(input("enter your age : \n"))

# if (age<13):
#     print("CHILD")
# elif (age<20):
#     print("TEENAGER")
# elif(age<60):
#     print("ADULT")
# else:
#     print("SENIOR")

#PRINT THE MOVIE TICKET ACC. TO THE AGE :


# age = int(input("enter your  age: \n"))
# day = str(input("enter your day: \n "))

# price = 12 if age >=18 else 8

# if day == "wednesday":
#     price -= 2
#     # price = price - 2 
# print("THE TICKET PRICE IS YOU $",price)


#GRADE CALCULATOR:

# marks = int(input("enter your marks: \n"))

# if(marks>=101):
#     print("please verifing your marks again")
#     exit()


# if (marks>=90):
#     print("grade A")
# elif(marks>=80):
#     print("grade B")
# elif(marks>=70):
#     print("grade C")
# elif(marks>=60):
#     print("grade D")
# else:
#     print("grade  E")



#chech a fruit colour:

# fruit = "apple"
# colour = "yellow"

# if (fruit ==  "apple"):
#     if(colour == "green" ):
#         print("unripe")
#     elif(colour == "yellow" ):
#         print("ripe")
#     elif(colour == "brown"):
#         print("overripe")


# fruit = (input("enter your fruit  name:  \t"))
# colour = (input("enter your colour: \t"))

# if colour == "green":
#     print(f"the {fruit} is unripe")
# elif colour == "yellow":
#     print(f"the {fruit} is ripe")
# elif colour == "brown":
#     print(f"the {fruit} is overripe")




#suggest on activity based weather:

# weather = input("enter weather: \t")


# if weather == "sunny":
#     print("go  for a walk")
# elif weather == "rainy":
#     print("read a book")
# elif weather == "snowy":
#     print("make a snow man")


# weather = input("enter what type of weather:  \t")


# if (weather == "sunny"):
#     activity = "go for a walk"
# elif (weather == "rainy"):
#     activity = "read a book "
# elif (weather == "snowy"):
#     activity = "make a snow man"

# print(activity)



#transport mode selection:

# distance = int(input("enter your distance: \t"))

# if distance < 3:
#     transport =  "walk"
# elif distance <= 15:
#     transport = "bike"
# else:
#     transport = "car"


# print("AI  is recommandation is transport:", transport)



# coffee  customization:

# order_size = input("enter your size of coffee: \t")
# extra_shot = True

# if extra_shot :
#     coffee = order_size + "coffee with an extra shot"
# else:
#     coffee = order_size + "coffee"


# print("order:",coffee)



# leap year :

year = 2024

if (year % 400 ==0 ) or (year %4 == 0 and year %100 != 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
