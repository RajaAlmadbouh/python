##################### Problem Solving Q1 #####################

'''arr = [[1, 2, 2, 4, 3, 6],
       [5, 1, 3, 4],
       [9, 5, 7, 1],
       [2, 4, 1, 3]]

sumArr = list(set( arr[0] + arr[1] + arr[2] + arr[3] ))
print(sumArr)'''

##################### Problem Solving Q2 #####################

'''def deferante(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    defSet = set1.difference(set2)
    return sorted(defSet)

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 

print(deferante(list1,list2))'''

##################### Problem Solving Q3 #####################

'''def identical(set1,set2):
    return set1.intersection(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(identical(set1,set2))'''

##################### Problem Solving Q4 #####################

'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = list(set1) + list(set2)

print(set(set3))'''

##################### Problem Solving Q5 #####################

'''List1 = []

while True :
    try :
        numList = int (input("Enter number of List : "))
        break #break try (numList)
    except ValueError:
         print("Invalid input. Please enter NUMBERS.")

for i in range (0,numList):
    userInput = input(f"Enter Value{i+1} of List : ")
    List1.append(userInput)

print(list(set(List1)))'''

##################### Problem Solving Q6 #####################

#(I cannot understand the question or there is an error in it)

##################### Problem Solving Q7 #####################

def conv(tup):
    tupList = []
    for ele in tup:
        tupList.append(list(ele))
    return tupList

tup =  [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
print(conv(tup))


##################### Problem Solving Q8 #####################

