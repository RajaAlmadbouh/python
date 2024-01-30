'''num1 = int(input("enter first number : "))
op = input()
num2 = int(input("enter sacend number : "))

if op=="+" :
    print(f"{num1} {op} {num2} = ",num1+num2)
if op=="-" :
    print(f"{num1} {op} {num2} = ",num1-num2)
if op=="*" :
    print(f"{num1} {op} {num2} = ",num1*num2)
if op=="/" :
    print(f"{num1} {op} {num2} = ",num1/num2)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num1} is equal to {num2}")'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)


middle_num = (num1 + num2 + num3) - min_num - max_num


print("Numbers in ascending order:", min_num, middle_num, max_num)'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''day_number = int(input("Enter a number (1-7): "))


if day_number == 1:
    print("Sunday")
elif day_number == 2:
    print("Monday")
elif day_number == 3:
    print("Tuesday")
elif day_number == 4:
    print("Wednesday")
elif day_number == 5:
    print("Thursday")
elif day_number == 6:
    print("Friday")
elif day_number == 7:
    print("Saturday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''Task looooooooooooooooooooooooooooop'''

'''num = 1

while num<=10 : 
    print(num)
    num += 1'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''num = int(input("enter number : "))

for i in range(1,num+1,1):
    
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''for i in range (1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}",end="|")
    print()'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''numLine = int(input("Enter the number of line : "))

for i in range(1,numLine+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''sum=0
calNumber = int(input("Enter the number you want to add : "))
for i in range(1, calNumber + 1):
    sum += i
    print(i,end=" + ")
print("=",sum)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''count = 0
number = int(input("Enter number: "))

while number != 0:
    number //= 10
    count += 1

print(f"The number of digits in the entered number is: {count}")'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''for i in range(-10, 0):
    print(i)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''total = 0
count = 0

value = float(input("Enter a number (enter 0 to stop): "))

if value == 0:
    print("Error: The first value cannot be 0.")
else:
    while value != 0:
        total += value
        count += 1
        value = float(input("Enter a number (enter 0 to stop): "))

    average = total / count
    print("Average:", average)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''import math
pi = math.pi

def area (r):
     return pi*math.pow(r,2)

def cer (r):
    return pi*r*2

r = float(input("Enter reduase = "))

while r<=0 : 
     print("Enter the corect reduase !!!!!")
     r = float(input("Enter reduase = "))

print(area(r))
print(cer(r))'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''import string

def Chick_Pass(Pass):
    countLatter = 0
    pal = 0 # (#$%&...)
    Uperr = "QERTYUIOPASDFGHJKLZXCVBNM"
    numUperr = 0
    number = "123456789"
    numNumber = 0
    


    for i in Pass : 
        countLatter +=1
        if i==string.punctuation:
            pal+=1
        if i in Uperr:
            numUperr += 1
        if i in number:
            numNumber += 1

    if countLatter >= 8 and pal > 0 and numUperr > 0 and numNumber > 0 :
        return("acc")
    else:
        return("invalid")



chicker = True
while chicker :
    Pass = input("Enter the password : ")
    c = Chick_Pass(Pass)
    if c == "acc" :
        print(c)
        chicker = False
    



#Chick_Pass(Pass)'''

    


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''import string

def Chick_Pass(password):
    countLetters = 0
    numPunctuations = 0
    upper_case = "QERTYUIOPASDFGHJKLZXCVBNM"
    numUpper = 0
    numbers = "123456789"
    numNumbers = 0

    for char in password:
        countLetters += 1
        if char in string.punctuation:
            numPunctuations += 1
        if char in upper_case:
            numUpper += 1
        if char in numbers:
            numNumbers += 1

    if countLetters >= 8 and numPunctuations > 0 and numUpper > 0 and numNumbers > 0:
        return "acc"
    #else:
       # return "invalid"

chicker = True
while chicker:
    password = input("Enter the password: ")
    result = Chick_Pass(password)
    if result == "acc":
        print(result)
        chicker = False
    else:
        print("invalid")'''




''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''name = "Raja"
n = name[0]
a = name[1]
m = name[3]
e = name[3]

for i in range(0,4):
    print(name[i])'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''age1 = int (input("Enter age 1 = "))
age2 = int (input("Enter age 2 = "))
age3 = int (input("Enter age 3 = "))

big = 0
midd = 0
smoll = 0

if age1>age2 and age1>age3:
    big=age1
    if age2>age3:
        midd=age2
        smoll=age3
    elif age3>age2:
        midd=age3
        smoll=age2
if age2>age1 and age2>age3:
    big=age2
    if age1>age3:
        midd=age1
        smoll=age3
    elif age3>age1:
        midd=age3
        smoll=age1
if age3>age1 and age3>age2:
    big=age3
    if age1>age2:
        midd=age1
        smoll=age2
    elif age2>age1:
        midd=age2
        smoll=age1
print("bigger = ",big)
print("modd = ",midd)
print("smole = ",smoll)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''for i in range (1,6):
    for j in range (1,i+1):
        print(j,end="")
    print()'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''num = int (input("Enter the number = "))
sum = 0

for i in range (1,num+1):
    sum += i
print(f"The Sumation = {sum}")'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''x = ord("a")
print(x)
a = chr(65)
print(a)
name = "RaJa9*"
#n = name.upper()
#print(ord("b")>99)

def Upp(tet):
    copyTxt = ""
    for i in tet:
        if ord(i) >= 97 and ord(i) <= 122:
            copyTxt += chr(ord(i) - 32)  
        else:
            copyTxt += i

    return copyTxt

x = Upp("RaJa")
print(x)

var = input("Enter value : ")
print(var.isidentifier())'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''---------------------String-------------------------'''

'''string = "Hello, word!"

print(string.index("H"))
print(string[:])
print(string[5:9])
print(string[::-1])
print(string[::-2])
print(string[:7])
print(string[-9:-1])
print(ord("A")) # 65 (According to ascii code )
print(chr(65)) # A (is the inverse of the ord() function)
print(string.upper())# HELLO, WORD! (Is method in Python is used to convert all characters in a string to uppercas)
print(string.lower())# hello, word! (Is method in Python is used to convert all characters in a string to lowercas)
print(string.capitalize())# Hello, word! (Is method in Python is used to capitalize the first character of a string)
print(string.title())# hello, word! (Is method in Python is used to capitalize the first letter of each word in a string)
print(string.find("H"))# 0 (method in Python is used to search for a substring within a string, and returns the index of the first occurrence of the substring, if found. If the substring is not found, it returns -1)
print(string.find("h"))# -1






for i in range(0,len(string)):
    if string[i]==" ":
        print(i)
        break
    else:
        print("not found character")'''



''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''---------------------List-------------------------'''

'''list1 = [5,1.3,"python",[4,8,2.9]]
list2 = [11,7,55,90,0,25]
list3 = ["r","a","j","a"]

name = "Raja"
name_list = list(name)#convert form string to list

num = 15
num_list = list(range(1,num+1))


print(name_list)#result = ["R","a","j","a"]
print(num_list)#result = [1,2,3,...,15]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[2][1])#list of character(python)
print(list1[3])
print(list1[3][0])
print(list1[3][1])
print(list1[3][2])
print(len(list1))#number of list1 = 4
print(len(list1[2]))#numuber of list1 in index 2 (python) = 6
print(list1[:3])#forword index
print(list1[:-1])#backword index
print(list1[-1::-1])#backword index
#----------bulit in function----------
print(len(list1))
print("befor sorted " , list3)
print("after sorted " , sorted(list3)) #This function does not modify the current value of list
print(sorted(list2,reverse=False))
print(sorted(list2,reverse=True))
print(sorted(list2))
print(max(list2))
print(min(list2))
print(sum(list2))
#----------methoud function----------
#help(list) #It gives the user all the methods used in the list
list4 = [1,"Raja","noor",[1.7,8],False]
list4.append([4,5])
list4.append("rend")

#list4.extend([9,0])
#list4.extend("rend")

list4.insert(1,"Zekoo")

print(list4)
print(list4.index([1.7,8]))
print(list4.index("Raja"))'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''----------------------tuple----------------------'''


'''tuple1 = (1,5,5,4,6,3,2,5,6)


print(tuple1.count(5))
print(tuple1.index(5))
print(max(tuple1))
print(len(tuple1))
print(min(tuple1))
print(sum(tuple1))

print(tuple1)
print(sorted(tuple1)) # [1, 2, 3, 4, 5, 5, 5, 6, 6] Arranges the elemant tuple , print tuple convert to list

sorted_tuple = sorted(tuple1)
print(type(tuple1)) # <class 'tuple'>
print(type(sorted_tuple)) # <class 'tuple'>







#print(tuple1.index("raja")) #Error ValueError: tuple.index(x): x not in tuple
#print(tuple1.index(9))

'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''----------------------set----------------------'''


'''
set1 = {1,2,3,"raja"}

print(set1)
#print(set1[0]) # Error the set has no index

for i in set1:  
    print(i) # the set stores elemants randomly

# set لا يمكن تعديل على قمية من عناضر  
# set يمكن اضافه او حذف على 
# set لا تكرر عناضر المتساوية
    
set1.add("Rand")
print(set1) #{1, 2, 3, 'Rand', 'raja'} add elemant in set

set2 = set1 # The process of equating a set, regardless of whether it is modified to set1 or set2, adds the same elements to them

set1.add("123456") # add set1 and set2 ("123456")
set2.add("S2") #  add set2 and set1 ("123456")
print(set1) # {1, 2, 3, 'S2', 'Rand', '123456', 'raja'}
print(set2) # {1, 2, 3, 'S2', 'raja', '123456', 'Rand'}

print(10*"-","set.copy",10*"-")

set3 = set1.copy() # The process of equating a set, Each set is modified independently
print(set3) # {1, 2, 3, 'raja', 'S2', '123456', 'Rand'}
set3.add("333333333")

print("set1 = ",set1) # {1, 2, 3, '123456', 'S2', 'Rand', 'raja'}
print("set3 = ",set3) # {'Rand', 1, 2, 3, '333333333', '123456', 'raja', 'S2'}

print(10*"-","set.diference",10*"-")

mark1 = {10,15,10,46,63,98,56,4,4}
mark2 = {10,33,46,34}

print(mark1.difference(mark2)) # {98, 4, 15, 56, 63} Stored items mark1 not found mark2
mark2.difference_update(mark1) # We modified mark2 and took different values from mark2
print(mark2) # {33, 34}

mark1.discard(10) # all element in mark1 without 10
print(mark1) # {98, 4, 56, 63, 46, 15}

#mark1.intersection(mark2)
print(mark1.intersection(mark2)) # mark2 و  mark1 الاشياء المشتركه   
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''----------------------dictionary----------------------'''

'''studant  = {"name" : "Raja" , "Age":18 , "Marks":[50,60,70,80]}
print(studant["name"]) # Raja
print(studant["Age"]) # 18
print(studant["Marks"]) # [50, 60, 70, 80]
print(studant["Marks"][0]) # 50
print(studant["Marks"][1]) # 60

studant["city"] = "irbid" # add Iteam in dictionary
print(studant) # {'name': 'Raja', 'Age': 18, 'Marks': [50, 60, 70, 80], 'city': 'irbid'}

studant["Age"] += 1
print(studant) # {'name': 'Raja', 'Age': 19, 'Marks': [50, 60, 70, 80], 'city': 'irbid'}

del studant["city"] # Remove Iteam
print(studant) # {'name': 'Raja', 'Age': 19, 'Marks': [50, 60, 70, 80]}

#studant.popitem() # delete last Item

print(studant.keys()) # dict_keys(['name', 'Age', 'Marks'])
print(studant.values()) # dict_values(['Raja', 19, [50, 60, 70, 80]])
print(studant.items()) #dict_items([('name', 'Raja'), ('Age', 19), ('Marks', [50, 60, 70, 80])])



for i in range(len(studant["Marks"])) : 
    print(studant["Marks"][i])

for key,value in studant.items():
    print(key," : ",value)

print("-------------------------------")

for key in studant.keys():
    print("Key = ",key)'''

#print("-------------------------------Task")


''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''string = input("Enter a string : ")
setString = set()
count = 0
UniqueString = ""

for char in string : 
    if char not in setString:
        setString.add(char)
        UniqueString += char

print("Unique string = ",UniqueString)
print("Number string = ",len(UniqueString))'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'FiŌy': 50}

dict3 = {}

for key , value in dict1.items():
    dict3[key] = value
for key , value in dict2.items():
    dict3[key] = value

print(dict3)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''dict1 = {0 : " " ,1 : ".,?!:", 2 : "ABC", 3 : "DEF", 4 : "GHI", 5 : "JKL", 6 : "MNO", 
         7 : "PQRS", 8 : "TUV", 9 : "WXYZ"}
mass = ""

while True:
    try:
        num = int(input("Enter number (0-9) : "))
        if 0 <= num <= 9: 
            char = dict1[num]
            print(char)
            break
        
        else:
            print("Invalid input. Please enter number from (1-9) .")
    except ValueError:
        print("Invalid input. Please Enter Only Number .")'''
    
              




# except ValueError:
# print("Invalid input. Please enter valid numerical values.")'''



    





''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''----------------------pandars----------------------'''
'''import numpy as np

studant = ["Raja" , "Zekoo" , "Osama" , "Sharaf" , "Ghith"]
studantArray = np.array(studant)

print(studantArray)
print(type(studantArray))

print("-"*50)

import pandas as pd
studantPandas = pd.Series(studant)

print(studantPandas)
print(type(studantPandas))

print("-"*50,"List")

mark = [ 45.5 , 65.8 , 34.6 , 98.5 , 34.7 ]
name = [ "python" , "OOP" , "Cal" , "DataManing" , "IS"]

markList = []
for i in mark:
    markList.append(int(i))

print(markList)

markList2 = [int(i) for i in mark]

print(markList2)

print("-"*50)

markS = pd.Series(markList2)
print(markS)
markS = pd.Series(markList2 , index=name)
print(markS)

print("-"*50,"Dictionary")

dict1 = {"python" : markList2[0] , "OOP" : markList2[1] ,"Cal" : markList2[2] ,
         "DataManing" : markList2[3] ,"IS" : markList2[4] }
dictS = pd.Series(dict1)
print(dictS)

print("-"*50,"Method Padnas")

grade = [ 44.5 , 34.4 ,  76.8 , 99.4 , 99.4]
nameGrade = ["c++" , "c#" , "Cal2" , "DataStrcure" , "DSS"]
gradeS = pd.Series(grade , index = nameGrade)
print(gradeS)
print("-"*25)

print(gradeS.value_counts())
print("-"*25)

print(gradeS.dtype)
print("-"*25)

print(gradeS.unique)
print("-"*25)

print(gradeS.mean())
print("-"*25)

print(gradeS.max())
print("-"*25)

print(gradeS.min())
print("-"*25)

print(gradeS.sum())
print("-"*25)

print(gradeS.product())
print("-"*25)

print(gradeS.count())
print("-"*25)

print(gradeS.shape)
print("-"*25)

print(gradeS.describe())
print("-"*25)

print(gradeS.index)
print("-"*25)

print(gradeS.values)
print("-"*25)

print(gradeS.sort_index())
print("-"*25)

print(gradeS.sort_values())
print("-"*25)

print(gradeS.sort_values(ascending=False))
print("-"*25)

print(gradeS)
gradeS.sort_values(ascending=False , inplace=True)
print(gradeS)
print("-"*25)'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''---------------------- X AND O Game ----------------------'''




''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''def createN (s1,s2):
    if len(s1)%2 == 0:
        return s1[:int(len(s1)/2)] + s2
    else:
        return s1[:int(len(s1)/2+1)] + s2


s1 = input("string1 = ")
s2 = input("string2 = ")

print(createN(s1,s2))'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''def cahrr (s1):
    Lo = ""
    Up = ""
    for i in s1:
        if 65 <= ord(i) and ord(i) <= 90:
            Up += i
        elif 97 <= ord(i) and ord(i) <= 122:
            Lo += i
    print(Lo + Up)
            

s1 = input("Enter the string : ")
cahrr(s1)'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''import string

def cahrr (s1):
    Chars = 0
    Digits = 0
    Symbol = 0
    for i in s1:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            Chars += 1
        elif i in string.punctuation:
            Symbol += 1
        elif i in "0123456789":
            Digits += 1

    print("Caracter = ",Chars)
    print("Digits = ",Digits)
    print("Symbol = ",Symbol)
            

s1 = input("Enter the string : ")
cahrr(s1)'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''def findd (s1,s2):
    if s2.find(s1) != -1 :
        print("True")
    else:
        print("False")

s1= input("enter string1 = ")
s2= input("enter string2 = ")
findd(s1,s2)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''def findd(s1):
    count = 0
    chick = True

    while chick:
        if s1.find("SDK") != -1 or s1.find("sdk") != -1:
            count += 1
        else:
            chick = False
    print(count)

s1= input("Enter String = ")
findd(s1)'''

'''def findd(s1):
    count = 0
    start_index = 0

    while True:
        index = s1.lower().find("sdk", start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1

    print("Number of occurrences of 'SDK' or 'sdk' in the string:", count)

s1 = input("Enter String: ")
findd(s1)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''def summ (s1):
    sum = 0
    count = 0
    charr = "0123456789"
    for i in s1 :
        if i in charr:
            sum += int(i)
            count += 1
    print("Sum is: 38 Average is = ",sum/count)
    
s1 = input("Enter String : ")
summ(s1)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''import string

def convert(s1):
    for i in s1:
        if i in string.punctuation:
            i = "#"
        print(i,end="")

s1 = input("Enter String = ")
convert(s1)'''


''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

#----------------midProjct----------------

'''print(30 * "-", "Welcome to FasterTaxi", 30 * "-")

while True:
    chooseType = input("""You can choose the type of service : 
                       1- Taxi 
                       2- Shared transfer
                       Enter the ID number for the service type : """)

    if chooseType == "1" or chooseType.lower() == "taxi":
        print("Taxi")
        captain = [["Toyota Avalon","Raja Almadbouh","80081","0796329390"],["Chevrolet Menlo","Montasr Asmer","17785","0772182104"]]
        
        print("Choose the type of car you prefer : ")

        for i in range(0,len(captain)):
            print(i+1,"- ",captain[i][0])

        while True:
            chooseCaptain = input("Enter the ID number for the Car type : ")
            
            if chooseCaptain == "1":
                print("""CarType\t  \tNameCaptain\t  \tPlateNumber\t  \tNumberCaptain\t  \t""")
                for i in range(0,len(captain[0])):
                    print(captain[0][i],end="\t\t")
                #print(captain[0][0])
                break
            elif chooseCaptain == "2":
                print("""CarType\t  \tNameCaptain\t  \tPlateNumber\t  \tNumberCaptain\t  \t""")
                for i in range(0,len(captain[1])):
                    print(captain[1][i],end="\t\t")
                #print(captain[1][0])
                break
            else:
                print("Choose wrong. You must enter a valid ID")



        break
    elif chooseType == "2" or chooseType.lower() == "shared transfer":
        print("Shared transfer")
        break
    else:
        print("Invalid input. Please enter 1 for Taxi or 2 for Shared transfer.")




'''



'''import random
print(30 * "-", "Welcome to FasterTaxi", 30 * "-")

while True:
    chooseType = input("""You can choose the type of service : 
                       1- Taxi 
                       2- Shared transfer
                       Enter the ID number for the service type : """)
    print()

    if chooseType == "1" or chooseType.lower() == "taxi":
        print("Taxi")
        print()
        captain = [["Toyota Avalon", "Raja Almadbouh", "80081", "0796329390"],
                   ["Chevrolet Menlo", "Montasr Asmer", "17785", "0772182104"]]

        print("Choose the type of car you prefer : ")

        for i in range(0, len(captain)):
            print(f"{i + 1}- {captain[i][0]}")
        
        print()

        while True:
            chooseCaptain = input("Enter the ID number for the Car type : ")

            if chooseCaptain == "1" or chooseCaptain == "2":
                print("{:<15}\t{:<15}\t{:<15}\t{:<15}".format("CarType", "NameCaptain", "PlateNumber", "NumberCaptain"))
                for i in range(0, len(captain[int(chooseCaptain) - 1])):
                    print("{:<15}\t".format(captain[int(chooseCaptain) - 1][i]), end="")
                print()
                print()
                print("""Do you want :
 1- Open flight
 2- trip (repel reply)""")
                print()
                priceKilo = 0.2
                priceTime = 0.05
                while True:
                    chooseUser = input ("Enter the ID number what you want : ")
                    if chooseUser == "1" :
                        print("Open flight \n ")
                        print ("Price per kilo   = ",priceKilo," JD")
                        print ("Price per minute = ",priceTime," JD")
                        print("\n")
                        while True:
                            try:
                                numKilo = float(input("Enter the number of kilometers the user traveled on this trip : "))
                                numTime = float(input("Enter the number of minutes the user traveled on this trip    : "))

                                if numKilo < 0 or numTime < 0:
                                    print("Please enter non-negative values for kilometers and minutes.")
                                    continue  

                                break  

                            except ValueError:
                                print("Invalid input. Please enter valid numerical values.")
                        priceTrip = numKilo*priceKilo + numTime*priceTime
                        print("\n")

                        if priceTrip < 1 :
                            priceTrip = 1
                            print("Minimum trips = 1 JD")

                        print("We wish you a happy trip with captain ",captain[int(chooseCaptain) - 1][1])
                        print("Total price of the trip = ",priceTrip," JD")
                        break
                    elif chooseUser == "2":
                        print("trip (repel reply) \n")

                        print("Note : To activate this service correctly, the trip must exceed a distance of 10 km")
                        print(f"(repel : The price starts at {priceKilo} km and {priceTime} minutes until the end of the first location)")
                        print("The writer takes 40% percent of the value of the first trip")

                        try:
                            print()
                            numKilo1 = float(input("Enter the number of kilometers the user traveled on the first trip:"))
                            numKilo2 = float(input("Enter the number of kilometers the user traveled on the second trip:"))
                            numTime1 = float(input("Enter the number of minutes the user traveled on the first trip    : "))
                            numTime2 = float(input("Enter the number of minutes the user traveled on the second trip   : "))
                            trailingTime = 0
                            trailingSpace = 0


                            if numKilo1 < 0 or numTime1 < 0 or numKilo2 < 0 or numTime2 < 0:
                                    print("Please enter non-negative values for kilometers and minutes.")
                                    continue  
                            
                            if numKilo1 < 10:
                                priceTrip = priceKilo*(numKilo1+numKilo2) + priceTime*(numTime1+numTime2)
                                print(priceTrip)
                                break
                            else:
                                if numKilo1 == numKilo2 or numKilo1 > numKilo2:
                                    priceTripKilo = numKilo1*priceKilo 
                                    priceTripKilo += priceTripKilo*0.4
                                elif numKilo1 < numKilo2 :
                                    trailingSpace = numKilo2 - numKilo1
                                    priceTripKilo = numKilo1*priceKilo + (numKilo1*priceKilo)*0.4 + trailingSpace*priceKilo 
                                    
                                
                                if numTime1 == numTime2 or numTime1 > numTime2:
                                    priceTripTime = numTime1*priceTime
                                    priceTripTime += priceTripTime*0.4
                                elif numTime1 < numTime2 : 
                                    trailingTime = numTime2 - numTime1
                                    priceTripTime = numTime1*priceTime + (numTime1*priceTime)*0.4 + trailingTime*priceTime
                                
                                priceTrip = priceTripKilo + priceTripTime
                                
                                print("Distance traveled (repel)             : ",numKilo1 , "KM => ",round(numKilo1*priceKilo,2),"JD")
                                if trailingSpace > 0:
                                    print("Trailing distance (out of bounds)     : ", trailingSpace,
                                          "KM =>", trailingSpace * priceKilo, "JD")
                                print("Distance traveled (reply)             : ",numKilo2 , "KM => ",round((numKilo1*priceKilo)*0.4,2),"JD")


                                print("time cut off (reply)                  : ",int(numTime1) , "Minutes =>",round(numTime1*priceTime,2),"JD")
                                if trailingTime > 0:
                                    print("Excessive time (out of bounds)        : ",int(trailingTime),"Minutes =>",round(trailingTime*priceTime,2),"JD")
                                print("time cut off (reply)                  : ",int(numTime2) , "Minutes => ",round((numTime1*priceTime)*0.4,2),"JD")

                                print("                                     ----------------------------------Total\n",
                                      "                                       Total = ",priceTrip)
                                 
                        except ValueError:
                                print("Invalid input. Please enter valid numerical values.")


                        break
                    else:
                        print("Choose wrong. You must enter a valid ID")
                      

                break
            else:
                print("Choose wrong. You must enter a valid ID")

        break
    elif chooseType == "2" or chooseType.lower() == "shared transfer":
        print("Shared transfer")

        places = {"Amman" : [ ["Toyota Avalon", "Raja Almadbouh", "80081", "0796329390",random.randint(1, 3)],
                              ["Chevrolet Menlo", "Montasr Asmer", "17785", "0772182104",random.randint(1, 3)] ],

                  "Irbid" : [ ["Fox ID4", "Mahmood AboDhase", "80044", "0755644887",random.randint(1, 3)],
                              ["Toyota Camry", "Osama Owadate", "14465", "0793746845",random.randint(1, 3)] ] }
        count = 0
        print("Choose the place you want to go to : ")
        for i in places.keys():
            count += 1
            print(count," - ",i)

        while True:
            chooseUser = input("Enter the ID number place you want to go to : ")
            
            if chooseUser == "1" or chooseUser == "Irbid" or chooseUser == "2" or chooseUser == "Amman" :
                if chooseUser == "1":
                    chooseUser = "Irbid"
                elif chooseUser == "2":
                    chooseUser = "Amman"
                
                print("")
                for i in range(len(places[chooseUser])):
                    print(i+1,"- ",places[chooseUser][i][0])
                    print("Number of seats reserved = ",places[chooseUser][i][4],"  ","Number of empty seats    = ",4-places[chooseUser][i][4])
                    print()
                
                while True:
                    chooseCar = input("Choose the type of car you prefer : ")

                    if 1 <= int(chooseCar) <= len(places[chooseUser]):
                        chosseCarInfo = places[chooseUser][int(chooseCar) - 1]
                        
                        print("\nChosen Car Information:")
                        print("Car Type             :", chosseCarInfo[0])
                        print("Driver               :", chosseCarInfo[1])
                        print("Plate Number         :", chosseCarInfo[2])
                        print("Driver's Phone Number:", chosseCarInfo[3])
                        #print("Reserved Seats:", chosenCarInfo[4])
                        print("Empty Seats          :", 4 - chosseCarInfo[4])

                        #numSeat = 0

                        while chosseCarInfo[4] < 4:
                            while True:
                                try:
                                    numSeat = int(input("Enter the number of seats you will reserve: "))
                                    
                                    if 0 < numSeat <= (4 - chosseCarInfo[4]):
                                        chosseCarInfo[4] += numSeat
                                        print("Reservation successful.")
                                        print(f"Total reserved seats: {chosseCarInfo[4]}")
                                        
                                        if chosseCarInfo[4] == 4:
                                            print("The number of seats is complete")
                                            print(f"Seat price for {numSeat} seats = {numSeat * 4} JD")
                                        break
                                    else:
                                        print(f"Invalid input. Please enter a number between 1 and {4 - chosseCarInfo[4]}.")
                                except ValueError:
                                    print("Invalid input. Please enter a valid number.")

                            if chosseCarInfo[4] < 4:
                                another_reservation = input("Do you want to make another reservation? (yes/no): ").lower()
                                if another_reservation != 'yes':
                                    break

                        if chosseCarInfo[4] == 4:
                            print("All seats are reserved.")
                            print(f"Total price for all reserved seats: {chosseCarInfo[4] * 4} JD")
                        break
                    else:
                        print("Choose wrong. You must enter a valid ID")
                break
            else :
                print("Invalid input. Please enter crrouct ID number of car.")
        break
    else:
        print("Invalid input. Please enter 1 for Taxi or 2 for Shared transfer.")'''










