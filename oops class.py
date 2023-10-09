
class calculation1:
    def add(self,a,b):
        return a+b
class calculation2:
    def multiplication(self,a,b):
        return a*b
class calculation3():
    def substraction(self,a,b):
        return a-b
class calculator(calculation1,calculation2,calculation3):
    def divide(self,a,b):
        return a/b
d=calculator()
print(d.add(10,20))
print(d.multiplication(10,80))
print(d.substraction(20,4))
print(d.divide(10,20))