class User():
    def __init__(self,name,pas):
        self.Name = name
        self._Password =pas
    def __str__(self):
        return f"UserName : {self.Name} \n "
    def getPassword(self):
        return self._Password
    def setPassword(self,newPassword):
        self._Password = newPassword

class captain(User):
    def __init__(self,typeCar,name,plate,phone):
        self.TypeCar = typeCar
        self.Name = name
        self.Plate = plate
        self.Phone = phone
    def __str__(self):
        return f"Car Type: {self.TypeCar}, Name: {self.Name}, Plate Number: {self.Plate}, Contact Number: {self.Phone}"
    
CaptainData = [] # data opject in class captain


C1 = captain("Toyota Avalon", "Raja Almadbouh", "80081", "0796329390")
C2 = captain("Chevrolet Menlo", "Montasr Asmer", "17785", "0772182104")
print(C2.getPassword())

CaptainData.append(C1)
CaptainData.append(C2)
    
