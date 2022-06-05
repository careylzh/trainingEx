import os #some geniuses wrote functions for us to use.
#so we just import the os module and call functions like below

# print(os.getcwd())

#os.chdir() - Change directory 
#os.mkdir('C:\\Users\\caris\\Desktop\\new_folder')
#for windows, this pattern is the safest for referencing a folder path
#online help source: https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca#:~:text=doubling%20the%20backslashes%3A-,data%20%3D%20open(%22C%3A%5C%5CUsers%5C%5Cmiche%5C%5CDocuments%5C%5Cschool%5C%5Cjaar2%5C%5CMIK%5C%5C2.6%5C%5Cvektis_agb_zorgverlener%22),-Edit%3A

#list_of_files = os.listdir('C:\\Users\\caris\\Desktop')
#print(list_of_files[1]) #see second file in desktop, alphabetical order
#os.remove('C:\\Users\\caris\\Desktop\\testing_new.txt')
#current working directory, meaning current _FilterChain

#Revision note: Slide 151 in Course Slides is extremely relevant to you 
# string_path1 = 'C:\\Users\\'
# string_path2 = '\\folder1'
# os.path.join(string_path1, string_path2)

# #the line below is called a file handler. Always the first step to open a new file
# random_text_file = open('C:\\Users\\caris\\Desktop\\test.txt','w') #step 1: open the file and state the purpose: read or write or append?
# for i in range(10): #do the processing
#     random_text_file.write("This is a line overwritten by python for loop")
# random_text_file.close() #close the file

#Ex: Write data to file, Slide 158
#1. use input() to prompt user for value, store in variable
#2. write bmi function
#3. write the variable into a file (quite a few lines)

# name = input('Enter name: ')
# height = float(input('Enter height (m): '))
# weight = float(input('Enter weight (kg): '))
# bmi = weight/(height*height)


# print(name, height, weight)

# #revise string substitution 
# # name		height	weight	bmi
# # alfred	    1.7		72.3	25.02
# with open('C:\\Users\\caris\\Desktop\\new_exercise_file_writing.txt', 'w') as f:
#     f.write("name   height  weight  bmi \n")
#     f.write('{} {} {} {}'.format(name, height, weight, bmi))
# f.close()

#VERY IMPT for your usage
import pandas as pd
spreadsheet_content = pd.read_csv("C:\\Users\\caris\\Desktop\\Sample-Spreadsheet-10-rows.csv", encoding= 'unicode_escape')
print(spreadsheet_content)

#Additional materials for pandas
#https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/
#https://blog.finxter.com/wp-content/uploads/2020/04/image-3-1024x791.png

import pandas as pd
cars_spreadsheet = pd.read_csv('C:\\Users\\caris\\Desktop\\PythonTraining-master\\exercises\\archive\\mtcars.csv', encoding= 'unicode_escape')
print(cars_spreadsheet[(cars_spreadsheet.hp>100) & (cars_spreadsheet.hp < 200)])


