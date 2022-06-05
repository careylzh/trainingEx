#OBJECT ORIENTED PROGRAMMING: new programming concept
# class Animal:
#     legs = 4
#     color = ''

#     def eat(self):
#         print('this animal is eating...')
    
#     def grooming(self):
#         print('this animal is being groomed right now')

#     def exercise(self):
#         print('this animal is exercising with the trainer')

#this template class Animal has 2 variables and 3 functions within it!

# dog = Animal() #a dog is an animal after all. got 4 legs and move similarly
# print(dog.color)
# print(dog.exercise())

# class Counter:
#     count = 0
#     #has 3 functions

#     def increase_count(self):
#         self.count = self.count + 1

#     def increase_count_n(self, N):
#         self.count = self.count + N
    
#     def reset_zero(self):
#         self.count = 0

# counter_instance = Counter() #create a copy of the template class Counter
# counter_instance_2 = Counter()

# print("instance1's count value before increase: ", counter_instance.count)
# counter_instance.increase_count()
# print("instance1's count value after increase: ", counter_instance.count)
# print(counter_instance_2.count)


# class Account:

#     shared_account = 200 #class variables, so any instance can access the same amount 
#     def __init__(self, balanceStart):
#         self.balance = balanceStart

#     def change_balance(self, n):
#         self.balance = self.balance + n

# carissa_acc = Account()
# carey_acc = Account()

# carissa_acc.change_balance(5000)
# print('carissa acc:', carissa_acc.balance, 'carey acc: ', carey_acc.balance)

'''
Object-oriented Programming
1. The idea of representing real-world objects in code
2. can contain multiple variables and multiple functions within in!
real world examples, classes Animal, Account, Counter
3. initializer
'''

#initializer 
class UpdatedAnimal:
    #initialiser, special function
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def eat(self):
        print('this animal is eating...')
    
    def grooming(self):
        print('this animal is being groomed right now')

    def exercise(self):
        print('this animal is exercising with the trainer')

    # def __del__(self):
    #     print("the cat has sadly passed away")

#uncomment for contructor example
# cat = UpdatedAnimal('ginger', 5)
# print(cat.color)

#OOP subconcept: inheritance
#child inherit the money/debt from parents' will. 
#in programming also - child class(in case Dog) can inherit properties from a parent class (in this case UpdatedAnimal)
#example also demonstrates OOP subconcept: Polymerism - similar objects can still have differences, eg. def talk() is implemented differently
class Dog(UpdatedAnimal):
    def talk(self):
        print('Bark at stranger at doorstep')

class Cat(UpdatedAnimal):
    def talk(self):
        print('gently purr')

chiwawa = Dog('brown', 4)
print(chiwawa.color)

