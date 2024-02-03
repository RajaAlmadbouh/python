class Studant : 
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
print("Email : ",Stu.Email)