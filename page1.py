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

import string

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
    



#Chick_Pass(Pass)

    


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

