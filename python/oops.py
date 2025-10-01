
# question:

# class car:
#     def  __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def show_detail(self):
#         print("the car brand is: " +self.brand)
#         print("the car model is: " +self.model)

# my_car= car("ford","mustang")
# my_car2 = car("tata", "safari")
# # result =  car1.show_detail()
# # print(result)
# my_car.show_detail()
# my_car2.show_detail()

# question:

# class student:
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks

#     def show_detail(self):
#         print("the student name is: " +self.name)
#         print("the student marks is: " +str(self.marks))
#         if self.marks >=30:
#             print("the student is pass")
#         else:
#             print("the student is fail")

# my_student = student("harsh",45)
# my_student2 = student("ram",23)
# my_student.show_detail()
# my_student2.show_detail()

# question:



# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show_detail(self):
#         print( f" NAME:{self.name} \n AGE:{self.age}")

# class student(person):
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age)
#         self.rollno = rollno
#         self.marks = marks

#     def student_info(self):
#         self.show_detail()
#         print("the student rollno is:"+str(self.rollno))
#         print("the student marks is: " +str(self.marks))

# p1 = person("rahul",12)
# p1.show_detail()

# print("----")



# s1 = student("HARSH VERMA",21,12,89)
# s1.student_info()

# question bankaccount:


# class bankaccount:
#     def __init__(self):
#         self.__balance = 0

#     def deposit_amount(self,amount):
#         if amount > 0:
#             self.__balance = amount
#             print(f"deposit: {amount}")
#         else:
#             print("deposit amount  must be positive")
    
#     def withdraw_amount(self,amount):
#         if amount >0:
#             if self.__balance >= amount:
#                 self.__balance -= amount
#                 print(f"withdraw: {amount}")
#             else:
#                 print("insufficient balance")
#         else:
#             print("withdraw amount must be positive")

#     def get_balance(self):
#         return self.__balance
    
# account = bankaccount()
# account.deposit_amount(10000)
# account.withdraw_amount(1000)
# print("current balance :",account.get_balance())



# question polymorphism:

# class animal:
#     def sound(self):
#         print("animal make a sound:")

# class dog(animal):
#     def sound(self):
#         print("dog says: bark! bark")

# class cat(animal):
#     def sound(self):
#         print("cat says: meow! meow")


# a = animal()
# b = dog()
# c = cat()

# a.sound()
# b.sound()
# c.sound()

# question  for polymorphism:



# class car:
#     def move(self):
#         print("car is moving on 4 wheels:")


# class bike:
#     def move(self):
#         print(" bike is moving on 2 wheels: ")


# def vehicle_move(vehicle):
#     vehicle.move()

# car1 = car()
# bike1 = bike()

# vehicle_move(car1)
# vehicle_move(bike1)














# maths question for   calculate a rectangle and circle:



# import math
# class shape:
#     def area(self):
#         print("the area is:")

# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius        
        
#     def area(self):
#          return math.pi*self.radius**2
        


# class rectangle(shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
    
    
    
#     def area(self):
#         return self.length * self.width
    
# shape = [rectangle(5,10), circle(7)]

# for shape in shape:
#     print(f"{shape.__class__.__name__}area:",shape.area())



with open("demo.txt","r") as file:
    data = file.read()
    print(data)

