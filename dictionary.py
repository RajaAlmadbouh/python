##################### Problem Solving Q1 #####################

'''def removeDic(dict1):
    neDict = {}
    for key,val in dict1.items():
        if val > 170 :
            neDict[key] = val
    return neDict

dict1 = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165,
'Pierre Cox': 190}

print(removeDic(dict1))'''

##################### Problem Solving Q2 #####################

'''def sorDict(dict1):
    list1 = []
    newDict = {}
    for val in dict1.values():
        list1.append(val)

    list1 = sorted(list1)

    for i in list1:
        for key,val in dict1.items():
            if val == i:
                newDict[key] = val
    
    print(newDict.items())


dict1 = {'Math':81, 'Physics':83, 'Chemistry':87}
sorDict(dict1)'''

##################### Problem Solving Q3 #####################

'''dict1 = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

for key, value in dict1.items():
    print(f"{key}: {value}")'''

##################### Problem Solving Q4 #####################

def getTopThree(dict1):
    list1 = []

    for i in dict1.values():
        list1.append(i)

    list1 = sorted(list1)
    for i in range(len(list1)-1, len(list1)-4, -1):
        for key, value in dict1.items():
            if value == list1[i]:
                print(f"{key} {value}")

dict1 = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
getTopThree(dict1)

##################### Problem Solving Q5 #####################

'''dict1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

uniVal = set()

for item in dict1:
    for value in item.values():
        uniVal.add(value)

print("Unique Values:", uniVal)'''