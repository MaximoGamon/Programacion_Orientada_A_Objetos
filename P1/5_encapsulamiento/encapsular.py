import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        return self.__color4
    
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def color(self,tamanio):
        self.__tamanio=tamanio


    def __getAtributoPrivado(self):
        return self._atributo_protegido
    
    def getAtributoprivado2(self):
        self.__getAtributoPrivado()
    
    def setAtributoPrivado(self,atributo_privado):
        self.__atributo_privado =atributo_privado

#Usar los atributos y metodos de acuerdo a su encapsulamiento
objeto=Clase("Rojo","Grande")
print(f"Mi objeto tiene los siguientes atributos {objeto.color} y {objeto.tamanio}")

print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atributo protegido: {objeto._atributo_protegido}")
print(f"Soy el contenido del atributo privado: {objeto.getAtributoprivado2()}")
objeto.setAtributoPrivado("Se ha cambiado el valor del atributo privado")
print(f"Soy el contenido del atributo privado: {objeto.getAtributoprivado2()}")
