# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model


# my_car = car("ford", "endavour")
# print(my_car.brand)
# print(my_car.model)

# task:

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("hello my name is: " + self.name)
#         print("my age is: " + str(self.age))


# p1 = person("harsh",21)
# p1.greet()


# task :

# class car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
#     def greet(self):
#         print("the car brand is:  "+self.brand)
#         print("the car model is: "+self.model)



# my_car = car("ford", "endavour")
# my_car.greet()


# task 3 : inheritance:

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
#     def greet(self):
#         print("the car brand is:  "+self.brand)
#         print("the car model is: "+self.model)

#     def fuel_type(self):
#          return "the fuel type is petrol or diesel"


# class ElectricCar(Car):
#         def __init__(self,brand,model,battery_size):
#             super().__init__(brand,model)
#             self.battery_size = battery_size
        
#         def fuel_type(self):
#              return "electric charge"

         

# my_tesla = ElectricCar("tesla","model S", "85KWH")
# # print(my_tesla.brand)
# # print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())
# my_tesla.greet()

# safari = Car("tata","safari")
# print(my_tesla.fuel_type())
# print(safari.fuel_type())











# task 4 :

# class animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         pass

# class dog(animal):
#     def make_sound(self):
#         return "bark"

# class cat(animal):
#     def make_sound(self):
#         return "meow"

# dog1 = dog("rocky","dog")
# cat1 = cat("kitty","cat")

# dog_sound = dog1.make_sound()
# cat_sound = cat1.make_sound()
# result = dog1.make_sound()
# result = cat1.make_sound()
# print("dog sound is: ",dog_sound)
# print("cat sound is: ",cat_sound)



#task of bank account:




class bankaccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        return(f"balance: {self.balance}")


    def __update_balance(self,amount):
        self.balance += amount
    
    def deposit(self,amount):
        if amount > 0:
            self.__update_balance(amount)
            return(f"deposited: {amount}")
        else:
            return("invalid deposit amount: ")
        
account = bankaccount()
print(account._show_balance())
print(account.deposit(500))

