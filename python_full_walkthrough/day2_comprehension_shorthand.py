print('hello world!')


#=========GENERATORS AND COMPREHENSION========
#purpose: to generate a list with some condition

# specialGeneratorList = [i**2 for i in range(1,11)]
# print(specialGeneratorList)

'''
conditions:
if eachNumber % 3 != and eachNumber % 5 != 0
'''
#eg. a != b 
#checking if a is not equal to b

specialList = [i**2 for i in range(1,21) if i % 3 != 0 and i % 5 != 0]
print(specialList)


#Exercise: Comprehension with string functions + list manipulation + string
#Thought process: guiding qns to guide your thinking
'''
what information(what data types) am I given?
what requirements(eg. must use comprehension)?
'''
#write your solution below

#what is the first thing I need to do?
#end result: is to get a list with:
#1. first letter of each word
#2. last letter of each word
#looks like...... ["Ty", "is", "a", "sy", "dy", 'ad', 'a', 'gt', 'dy']

'''
split()
how do I get the first letter? any method I learned before? If not, can I google this?
'''

# sentence="Today is a sunny day and a great day"
# words=sentence.split()
# specialList = [eachWord[0]:eachWord[-1] for eachWord in words ]
# print(specialList)

# #DoubleLoop in Comprehension explanation, slide 135
# [i*j for i in range(1,3) for j in range(1,5)]
# specialList = []

#same as
# for i in range(1,3):
#     for j in range(1,5):
#         specialList.append(i*j)

#Dictionary generated thru Comprehension method
name = ['Ally','Belinda','Steve']
height = [160,158,170]
specialDictionary = {name:height for name,height in zip(name,height)}
print(specialDictionary)
print(specialDictionary['Ally'])

#Slide 139: Exercise on Dictionary thru Comprehension Method
d1 = {'Tom': 14, 'Patrick': 12, 'Sean': 15}
d2 = {'Jeanne': 14, 'Marie': 12}
result = {'Tom': 14, 'Patrick': 12, 'Sean': 15, 'Jeanne': 14, 'Marie': 12}

# specialDictionary = {key:value for eachItem in (d1,d2) for key,value in eachItem.items()}

#line 66 has the same effect as this: 
specialDictionary = {}
for eachItem in (d1,d2):
    for key, value in eachItem.items():
        specialDictionary[key] = value

print(specialDictionary)

#Slides 140-147 in Tertiary Courses PDF: not crucial for learning for your first month

