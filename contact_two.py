#Question1: printing the local file

#creating the file
with open(r"full_name.txt","w") as f:
    f.write("John Ibe Divine")
#opening file
with open(r"full_name.txt","r") as f:
    fullName = f.read()
#printing full name
print(fullName)
#splitting names base on whitespace
first_name, surname, last_name = fullName.split(' ')
#printing names
print(f'First Name {first_name}')
print(f'Surname {surname}')
print(f'Last Name {last_name}')

#Question2: printing the local file
import os
file_path=os.getcwd()
print(f'The current file path is {file_path}')


#Question3: printing babies an in an html file
import re
with open(r"assignment\babies.html","r") as f:
    html_file = f.read()
            
            
reg = r'<td>[A-Za-z]+</td><td>[0-9,]+</td>'
matches = re.findall(reg, html_file)

for i in matches:
    print(f'Name {i[0]}')

#Question4: create a sorting algorithm
def sort(file):
    file.sort()
    print(file)
fruits = ['apple','mango','banana']

sort(fruits)