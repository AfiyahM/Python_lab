class area:
    def area(self,l,b):
        self.l=l
        self.b=b
        return l*b
    
class perimeter:
    def peri(self,l,b):
        self.l=l
        self.b=b
        sum=2*(l+b)
        return sum



class rect(area,perimeter):
    a=area(11,12)
    p=perimeter(11,12)
    












'''
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()'''