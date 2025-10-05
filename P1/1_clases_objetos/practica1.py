"""
Ejercicio Práctico #1 Implementar paradigma estructurado vs OO
"""

#Estructurada
def area_rectangulo(base,altura):
    return base * altura

print(area_rectangulo(5,3))

#Orientada a objetos
class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
rect = rectangulo(5,3)
print(rect.area())



