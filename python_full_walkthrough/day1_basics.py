
#this is a single-line comment. starts with a hash sign. not recognised by the program
'''
this is a
multi-line comment.
For you to take notes and for you to communicate with other developers.
The python program ignores comments
'''
# print("hello Carissa! from Carey's Macbook") 
# print('Hello Carissa')

#data types. like "containers" which store values
# string, number, so far...

# summary of learning in the first hour:setting up and general ideas, no syntax yet
'''
1. check if python interpreter is installed by windows search for python shell
my version was 3.10
2. what code editors(i.e. IDE) have I installed? Pycharm + Visual Studio(VS) Code
3. Installed Live Share extension in VS code for instructor remote access to my computer
'''

#============NUMBER===============
a = 5 
b = 6
#print(a+b) #we are printing the variables a + b, so no need wrap these variables with " "

a, b = 1,2
a,b = b,a+b #while a takes the value of b, the second part references the old value of a. That's why b = a + b  = 1 + 2 
#a = b 
#b = a + b
#what is the value of b?
#print(b)

# a = 3 
# b = 4
# c = a + b
# print( "{} = {} + {}".format(c,a,b) ) #this syntax is called string templating: substitute variable values into a string
a = 4.444
b = 5.555
c = 6.6666
d = a + b + c
#print("{} = {} + {} + {}".format(d,a,b,c))


#============STRING FUNCTIONS===============================
#simple formatting exercise - make all lowercase then can replace regardless of whether original input was upper/lower
c = "hEllO cAriSsA!"
# print(c.capitalize())
#print(c.upper())
c = c.lower()
#print("variable c after lower-casing, before making replacement: ", c)
#print(c.replace('carissa', 'Carey') )

capital = "paris"
country = "france"
country = country.upper()
capital = capital.capitalize()
# print("The capital of {} is {}".format(country, capital)) 
#notes for the exercise above
'''Thought process (step-by-step):
1. message has some uppercase, which variable? which function to use to make this variable uppercase? line 55'
2. What is the overall message structure? What was the syntax? String substitution print("".format(variable))
'''

a = 'Today is a sunny day' #string stored into the variable named a
b = a.split() #splits the variable 'a' into a LIST OF individual words (where each word is a variable type STRING)
#print(b)
#print(type(b)) #b is a list, new variable type, which stores individual words as strings 

a = "abc@def.com"
b = a.split("@") #splits the variable a at the '@' sign, stores into b as a list
#print(b)
# print('username: ', b[0]) #list referencing: reference a particular element in the list. First item is position 0
# print('domain name: ', b[1]) #reference second item in the list b

#print the username abc 
#print the domain name def.com separately

#CHECKPOINT: recap of morning
'''
what is python? General purpose - web development, data analysis, automation
setup - install python interpreter (to run your python code), IDEs(pycharm, visual studio code)
syntax - print, commenting, number, string formatting, string functions eg. something.upper()
'''

#==========LIST============
aList = ['hello', 'carissa', 'from', 'tertiary courses']
#positions : 0         1           2       3
# print(aList.index('carissa')) #locate the position of variable
indexedItem = aList.index('carissa')
#aList.append('new item') #adds a variable/input to the end of the list
#aList.insert(1,99)
#print(aList)

#list functions to remove elements in a list
#aList.remove('from') #removes some input, do not give position, give exact thing to remove
#print(aList)

poppedItem = aList.pop(2) #takes out the element at position 2, and stores into the variable poppedItem
# print(poppedItem) 

# list_of_numbers = [1,'hello',1,1,1,1,7,8,'carissa']
# print(len(list_of_numbers)) #gives us the size of the variable, 9 items so len() returns 9

# print(list_of_numbers.count(1))


letters=["A","C","C","A","T","T","G","A","C"]
#think step-by-step: what was the first task? count. what was the syntax to count [something] in a given list?
# print("number of A in original letters: ", letters.count("A"))
# print("position of first T in original letters: ", letters.index("T"))
# letters2 = letters.copy()
# letters2.remove("G")
# print("after removing G: ", letters2)
# letters2.insert(3, "A")
# print("after inserting A at position 3: ", letters2)
# letters2.reverse()
# print("reversed letters2: ", letters2)

#CHECKPOINT: what are the data types(variable types) we have come across?
'''

string "hello world, carissa!" 

number 1.1

list (of numbers) [1,2,3,5], list (of strings) ['hello', 'world'], or a mixture ['hello',1,1,1,1]

tuple (1,2,3,4,5) immutable: means cannot change after writing

'''

#========TUPLE======
aTuple = (1,2,3,4)
#difference from lists: lists can edit after writing eg. append, remove.
#tuple cannot edit after writing/declaring

#======DICTIONARY==========
#to associate values together, eg. country to respective clients
#explanation: capitals = { key1:value1, key2:value2, key3:value3}
capitals = {'France':'Paris', 'Germany':'Berlin', 'Italy':'Rome'}
#list referencing applies to dictionary referencing:
# print(capitals['France']) #should see paris. this is an example of dictionary referencing 

# sent = "Peter reads a book on a table"
# words = sent.split() #words = ['Peter', 'reads', 'a', 'book', 'on', 'a', table']
# vocab = set(words) #vocab = {'Peter', 'reads', 'a', 'book', 'on', table'}
# print(vocab) 
# print(len(vocab))

#QN: when to use which brackets? There are 3 types = () [] {}
'''
1. for functions, use normal bracket: print() count() capitalise()  
2. list/dictionary referencing (i.e. take an item in a list), use square brackets: aList[0], aDictionary['hello']
3. for defining sets/dictionaries, use curly brackets: aDictionary = {'Carissa': '1 day of experience in Python', 'Bill Gates': 'has 0 days of experience in python'}
'''

a = (1,2,3,4)
# print(2 in a) #prints True: 2 is indeed in the set a

#========CONTROL STRUCTURES=====================
'''
structures which help us control what happens
and when what happens

aka Loops
'''
#1.If-else
# a = 1
# b = 1
# if(a < b):
#     print("a is smaller than b")
# elif(a > b):
#     print("a is larger than b")
# else:
#     print("a is same as b")

# grade = input('What is your grade :' )
# print("user input: ", grade)
# if(grade == "A"):
#     print("Excellent!")
# elif(grade == "B"):
#     print("Well Done!")
# elif(grade == "C"):
#     print("Work Harder")
# else:
#     print("I don't know your grade")

order_total = 200 #order qty
#ternary operator: assigning value based on some other condition
discount = 25 if order_total > 100 else 0 
'''
same as: 

if order_total>100:
    discount = 25
else:
    discount = 0
''' 
#discount should only apply if order qty > 100, if not don't give discount
    
a = 1 
# while(a<10):
#     print(a)
#     a = a + 1

1,1,2,3,5,8
#GENERATING FIBBONACCCI SEQUENCE
'''
what do i need:?

'''
# first_number = 1 
# previous_number = 1
# next_num = 0
# counter = 0
# while(counter<10):

#     #what variables should i also update aside from next_num?
#     next_num = first_number + previous_number #definition of fibbo
#     first_number = previous_number #at each iteration, first_number is updated
#     previous_number = next_num
    
#     counter = counter + 1

#     print(next_num)

'''        
round 0: 1 1 2  
first_num=1, previous_number=1, next_num=2

round 1:   1 2 3 
first_num=previous_number = 1, previous_number= =2, next_num=3
round 2:    2 3 5 first_num=3, previous_number=5, next_num=8
round 3:      3 5 6 ...
'''

#3. For loop
aList = [3,4,5]
# for eachElement in aList:
# 	print(eachElement)
# for eachElement in range(1,6):
#     print(eachElement)



#QN: how do you export data to be used in your daily work? 
#Ans: KIV till module 8 

#CHALLENGE: use a for loop to generate first 10 squares 1,2,4,16,25,36...
# 1**2 2**2 ...
# aList = []
# for eachNumber in range (1,11):
#     print(eachNumber**2)
#     aList.append(eachNumber**2)

#Enumerate (advanced concept)
person = ['Alfred','Ally','Belinda']
height = [170,160,155]
weight = [60,55,45]    
# for eachPosition, eachName in enumerate(person):
    
#eachPosition 0 1 2
#eachName 'Alfred', 'Ally', 'Belinda'
# zippedVariable = zip(person,height,weight)
# for i,j, k in zippedVariable:
#     print(i,j,k)
# print(type(zippedVariable))

#demo of break: to exit a loop automatically, so no need to ctrl+c to interrupt manually
# a = 2 
# while (a < 10):
#     print(a)
#     if(a==2): break

# for x in range(1,5):
#     if(x==3):continue #skips all the code below when x == 3 
#     print("x = {}".format(x))

#generate prime number sequence
#what is is a prime number? A number that can only be divided by itself and 1 
# primeList = []
# for eachNumber in range (1,100):
#     for eachDivider in range (2, eachNumber):
#         if eachNumber % eachDivider == 0: break
#     else: primeList.append(eachNumber)
# print(set(primeList))
# 1 2 3 4 5 6 7 8 9 10
# 1,1 
# 1/2
# 1/1

# 2/1
# 2/2

# 3/1
# 3/2
# 3/3

# 4/1
# 4/2 


#=======FUNCTIONS==============
# def functionName(x,y,z):
#     sum_of_three_numbers = x + y + z
#     return sum_of_three_numbers
# print( functionName(1,2,3)   )

#write a function which takes in 4 inputs and calculates fare
# def taxifare(booking_fee, starting_price, cost_per_km, km):
#     sum_of_fixed_fare = booking_fee + starting_price
#     sum_of_variable_fare = cost_per_km*km
#     return sum_of_fixed_fare + sum_of_variable_fare

# print(taxifare(3.50, 2.30, 0.20, 1)      )

#MODULE 6: importing packages/libaries
# import time
# import math

# print('hello!')
# time.sleep(2) #pauses the code for 2 seconds
# print('5 seconds later...')
# import random
# die = random.choice([1,2,3,4,5,6])
# print(die)

# import importfile
# print(importfile.sumofthings(1,2,3))

# def f(x=3,y):
#     return x*y
# print(f(4))

# a=[1,2];b=[3,4];c=zip(b,a)
# for a,b in c:
#     print(a,b)

#SUMMARY OF DAY 1
'''
1. what is python? general purpose?
2. basic syntax:
    - 6 data types: Number, String, List, Dictionary, Set, Tuple
    - commenting
    - printing
    - respective data type functions eg. list functions , string functions
    - control structure (loops)
    - functions
'''

#Carissa says she remembers roughly 50%
'''
substitution: string formattting
nameOfStudent = 'Carissa'
print('Hello {}!'.format(nameOfStudent) )


6 data types - variable types in Python:
- for what? Store value
string
- string functions 
a.count()
a.capitalize()
a.lower()
a.upper()
a.split('@') eg. a = 'abc@def.com', if apply split [abc','def.com']

set eg. aSet = {1,2,3} 
- unordered, but list is ordered, elements of list got positions 

number eg. a=5

list eg. aList = [1,2,3,4,5,'hello']
aList.count('a')
aList.index('a') #gives you index of the value given 
aList[0]

dictionary: eg. singapore = {'pasir ris':'d-resort', 'hougang': 'kang kar mall'}
- it was meant to ASSOCIATE values together

tuple eg. tuple (1,2,2,3) != set {1,2,3}

#CONTROL STRUCTURES (aka loops)
#if-else
#while loop: while a condition is not satisfied, keep running some statements 

#for loop
for eachElement in someList:
    print(eachElement)

for eachNumber in range(1,5): #excluding 5, runs from 1 to 4 
    print(someList[eachNumber]) eg. first round is someList[1]


#Operators (math symbols for calculating something)
** exponent eg. 3**2 gives 9
/
+ 
== checking eg. if(a==b)

#FUNCTIONS
def functionName(input1, input2): #Camelcasing the functionName or you can do understyle score function_name
    #can also put more statements/formula here
    adding2Numbers = input1 + input2
    return adding2Numbers

import file: library python file created must be in the same folder as the using file

'''