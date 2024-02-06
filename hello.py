# # 2.3
# name = "jingyan"
# msg= f"Hello {name.title()}, welcome"
# print(msg)

# # 2.4
# name = "xu JIngyan"
# print(name.lower())
# print(name.upper())
# print(name.title()

# bikes=['trek','redline','specialized']
# msg=f"my first bike is {bikes[0].title()}"
# print(msg)

# message = input ('input something and i will send it back to you')
# print(message) 

# unconfirmed_users=['alice','brian','cadance']
# confirmed_users = []

# while(unconfirmed_users):
#     current_user=unconfirmed_users.pop()
#     print(f"Verifiing User: {current_user.title()}")

#     confirmed_users.append(current_user)

# print("\nThe following users have been verified:")
# for user in confirmed_users:
#     print(user.title())

# class Dog:
#     """class Dog"""

#     def __init__(self, name, age):
#         """初始化属性 name 和 age"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """模拟小狗收到命令时坐下"""
#         print(f"{self.name} is now sitting!")

#     def roll_over(self):
#         """模拟小狗收到命令时打滚"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie',8)
# print(f"{my_dog.name} is my dog's name.")
# print(f"My dog is {my_dog.age} years old.")

# my_dog.sit()
# my_dog.roll_over()
        

# class Car:

#     def __init__(self,make,year,model):
#         self.make=make
#         self.year=year
#         self.model=model
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name=f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """更新里程数，且禁止里程数往回调"""
#         if mileage < self.odometer_reading:
#             print("You cannot roll back an odometer!")
#         else:
#             self.odometer_reading = mileage
    
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# class Battery:
#     def __init__(self, battery_size=40):
#         self.battery_size=battery_size
    
#     def describe_battery(self):
#         print(f"This car has a {self.battery_size} -kWh battery.")

#     def get_range(self):
#         if self.battery_size == 40:
#             range=150
#         elif self.battery_size == 65:
#             range=225
#         print(f"This car can go about {range} miles ")

# class ElectricCar(Car):
#     def __init__(self, make, year, model):
#         super().__init__(make, year, model)
#         self.battery=Battery(65)

# my_leaf=ElectricCar("nissan",2014,"leaf")
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()


# from pathlib import Path

# def count_words(path):
#     try:
#         contents=path.read_text(encoding="utf-8")
#     except FileNotFoundError:
#         print(f"No such file {path}!")
#     else:
#         words=contents.split()
#         num_words=len(words)
#         print(f"This book has {num_words} words!")

# path = Path("alice.txt")
# count_words(path)


class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做好准备"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print("Survey_results")
        for response in self.responses:
            print(f"- {response}")




