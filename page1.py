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

for i in range (1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}",end="|")
    print()


