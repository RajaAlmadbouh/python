##################### Problem Solving Q1 #####################
'''def Multiply(list1):
    res = 1
    for item in list1:
        res *= item
    return res

List1 = []

while True :
    try :
        numList = int (input("Enter number of List : "))
        break #break try (numList)
    except ValueError:
         print("Invalid input. Please enter NUMBERS.")

for i in range (0,numList):
    while True :
        try : 
            userInput = int (input(f"Enter Value{i+1} of List : "))
            break#break try (userInput)
        except ValueError : 
            print("Invalid input. Please enter VALUE TO LIST.")
    
    List1.append(userInput)

print(List1)
print(f"result = {Multiply(List1)}")'''


##################### Problem Solving Q2 #####################

'''List1 = []

while True :
    try :
        numList = int (input("Enter number of List : "))
        break #break try (numList)
    except ValueError:
         print("Invalid input. Please enter NUMBERS.")

for i in range (0,numList):
    while True :
        try : 
            userInput = int (input(f"Enter Value{i+1} of List : "))
            break#break try (userInput)
        except ValueError : 
            print("Invalid input. Please enter VALUE TO LIST.")
    
    List1.append(userInput)

print("List = ",List1)
print("Largest = ",max(List1))
print("Smoller = ",min(List1))
print("Sumation = ",sum(List1))'''

##################### Problem Solving Q3 #####################

'''List1 = []

while True :
    try :
        numList = int (input("Enter number of List : "))
        break #break try (numList)
    except ValueError:
         print("Invalid input. Please enter NUMBERS.")

for i in range (0,numList):
    while True :
        try : 
            userInput = int (input(f"Enter Value{i+1} of List : "))
            break#break try (userInput)
        except ValueError : 
            print("Invalid input. Please enter VALUE TO LIST.")
    
    List1.append(userInput)

print(List1)

ListCopy = []
for item in List1:
   if item not in ListCopy:
       ListCopy.append(item)

print("Uniqe List : ",ListCopy)'''


##################### Problem Solving Q4 #####################
        
        
'''List1 = []

while True :
    try :
        numList = int (input("Enter number of List : "))
        break #break try (numList)
    except ValueError:
         print("Invalid input. Please enter NUMBERS.")

for i in range (0,numList):
    while True :
        try : 
            userInput = int (input(f"Enter Value{i+1} of List : "))
            break#break try (userInput)
        except ValueError : 
            print("Invalid input. Please enter VALUE TO LIST.")
    
    List1.append(userInput)

print(List1)

if len(List1) == 0 :
    print("List is EMPTY")
else:
    print("List is NOT EMPTY")'''

##################### Problem Solving Q5 #####################

'''List1 = [12,34,54,67,3,54,6]
List2 = [65,7,36,86,43,643,23,6]
chick = False

for item in List1:
    if item in List2:
        chick = True
        break
if chick:
    print(chick)
else :
    print(chick)'''

##################### Problem Solving Q6 #####################

'''List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del List[0]
del List[len(List)-2]
del List[len(List)-1]
print(List)'''

##################### Problem Solving Q7 #####################

'''List = ["R","a","J","a"]
s = "".join(List)

print("List   = ",List)
print("String = ",s)
'''