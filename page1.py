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

list1 = [5,1.3,"python",[4,8,2.9]]
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