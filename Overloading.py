''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''---------------------- Overloading ----------------------'''

'''#Overloading Arithmetic Operators

class point:

    def __init__(self,x=0,y=0):
        self.X = x
        self.Y = y

    def move (self,addX=0 ,addY=0):
        self.X += addX
        self.Y += addY
    
    def __str__(self):
        return f"{self.X} , {self.Y}"
    
    def __add__(self,OOpject): #OOpject (Lt is a opject from a class point i can put them together)
        self.X += OOpject.X
        self.Y += OOpject.Y
    
    def __iadd__(self,OOpject):
        self.X += OOpject.X
        self.Y += OOpject.Y  
        return self
    
    def __neg__(self):
        p3 = point()
        p3.X = self.X * -1
        p3.Y = self.Y * -1
        return p3
    
    def __invert__(self):
        p3 = point()
        p3.X = self.Y
        p3.Y = self.X
        return p3
    

p1 = point(4,7)
p2 = point(6,3)

    
print(p1)
#p1.move(4,3)
#print(p1+p2) #It is not permissible to collect Opject to Opject except by Overloading massege error TypeError: unsupported operand type(s) for +: 'point' and 'point'
p1 + p2
print(p1)

p1 += p2 # __iadd__
print(p1)

print(-p1)#__neg__
print(~p1)#__invert__

                                               #--------------Note--------------
# __add__() => +
# __sub__() => -
# __mul__() => *
# __div__() => /
# __mod__() => %
# __po__() => ** power
# __lt__() => <  less than
# __gt__() => >  grater than
# __le__() => <= less than or equal to
# __gr__() => >=  grater than or equal to
# __eq__() => ==  equality check
# __gt__() => !=  inequality check
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''

#-------------------------Task Overloading-------------------------

class Fraction:

    def __init__(self , numerator = 0 , denominator = 1):
        self.Numerator = numerator

        if denominator == 0 :
            self.Denominator = 1
        else:
            self.Denominator = denominator

    def __str__(self):
        return f"{self.Numerator} , {self.Denominator}"
    
    def __add__(self , OPP):
        self.Numerator += OPP.Numerator
        self.Denominator += OPP.Denominator
        return Fraction(self.Numerator,self.Denominator)
        
    
    def __iadd__(self , OPP):
        self.Numerator += OPP.Numerator
        self.Denominator += OPP.Denominator
        return self

    def __truediv__(self , OPP):
        self.Numerator /= OPP.Numerator
        self.Denominator /= OPP.Denominator
        return Fraction(self.Numerator,self.Denominator)
    
    def __mul__(self , OPP):
        self.Numerator *= OPP.Numerator
        self.Denominator *= OPP.Denominator
        return Fraction(self.Numerator,self.Denominator)

    def __lt__(self , OPP):
        return (self.Denominator/self.Numerator) < (OPP.Denominator/OPP.Numerator)
    
    def __gt__(self , OPP):
        return (self.Denominator/self.Numerator) > (OPP.Denominator/OPP.Numerator)
    
    def __le__(self , OPP):
        return (self.Denominator/self.Numerator) <= (OPP.Denominator/OPP.Numerator)
    
    def __gr__(self , OPP):
        return (self.Denominator/self.Numerator) >= (OPP.Denominator/OPP.Numerator)
    
    def __eq__(self , OPP):
        return (self.Denominator/self.Numerator) == (OPP.Denominator/OPP.Numerator)
    
    def __gt__(self , OPP):
        return (self.Denominator/self.Numerator) != (OPP.Denominator/OPP.Numerator)
    

    

    
f1 = Fraction(2,0)
f2 = Fraction(4,5)
print("calcolet =",f1+f2)
print("multiply = ",f1*f2)
print("divaided = ",f1/f2)
