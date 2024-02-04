'''class Studant : 
    courseName = "python"

    def __init__(self,name,track,email):
        self.Name = name
        self.Track = track
        self.Email = email

Sname = input("Enter Name = ")
Strack = input("Enter Track = ")
Semail = input("Enter Email = ")

while True:
    if Semail.endswith(".com"):
        Stu = Studant(Sname,Strack,Semail)
        break
    else:
        print("invalid Email")
        Semail = input("Enter Email = ")

#Stu = Studant(Sname,Strack,Semail)

print("Name : ",Stu.Name)
print("Track : ",Stu.Track)
print("Email : ",Stu.Email)'''

''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''

'''studant = { "Name" : ["Raja" , "Osama" , "Ghith" ] , 
            "Major" : ["CIS" , "Markting" , "CS"] }

class stuff():
    # class attribute
    time = "8:00AM - 3:00PM"
    univarsity = "SDK"

    # opject attribute
    def __init__(self,n,po,ide,pas,cor=[]):
        self.Name = n
        self.Postion = po
        self.__ID = ide
        self.__password = pas
        self.Corsues = cor

    def showStudant(self,studant):
        for i in studant.keys():
            print(i," : ",studant[i])
    
    def addCorsues(self,newCorsues):
        self.Corsues.append(newCorsues)
        print(self.Corsues)

oop = stuff("Omar","manager",1,"12345",["OOP"])
oop.showStudant(studant)
oop.addCorsues(["IS","Clacules 2","C++"])
'''

''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''

class GradeBook():
    Grade = {}

    def __init__(self,grade):
        self.Grade = grade

    def addStudant(self,name,grade):
        self.Grade[name] = grade

    def reportGrade(self,name):
        score = 0
        for val in self.Grade[name]:
            score += val
        if score == 0:
            print("This studant is not Exist")
        else:
            print(f"score {self.Grade[name]}= {score}")
    
    def avargeGrade(self):
        avg = 0 
        for item in self.Grade.values():
            for i in item:
                avg += i
        
        return avg/len(self.Grade)
    