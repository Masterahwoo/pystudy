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

class Dog:
    """class Dog"""

    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie',8)
print(f"{my_dog.name} is my dog's name.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
        
    