import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #metodo constructor para inicializar los valores de los atributos a la hora de crear o instanciar el objeto de la clase

     #Metodos o acciones o funciones que hace el objeto 
    #Crear los metodos getters y setters .- Estos metodos son importantes y necesarias en todas las classes para que el 
    #programador  interactue con los valores de los atributos a traves de estos
    #metodos... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get y/o)
    #para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto
    # En teoria se deberia de crear un metodo Getterss y Setters por cada atributo que contenga la clase
    #Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del
    #atributo o propiedad en cuestion

   def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
       self.__marca=marca
       self.__color=color
       self.__modelo=modelo
       self.__velocidad=velocidad
       self.__caballaje=caballaje
       self.__plazas=plazas

    #1er Forma
   def getMarca(self):
       return self.__marca
    
   def setMarca(self,marca):
       self.__marca=marca

    #2da forma
   @property
   def marca2(self):
      return self.__marca
    
   @marca2.setter
   def marca2(self,marca):
       self.__marca=marca=marca

   def getColor(self):
       return self.__color
    
   def setColor(self,color):
       self.__color=color

   def getModelo(self):
       return self.__modelo
    
   def setModelo(self,modelo):
       self.__modelo=modelo

   def getVelocidad(self):
       return self.__velocidad
    
   def setVelocidad(self,velocidad):
       self.__velocidad=velocidad

   def getCaballaje(self):
       return self.__caballaje
    
   def setCaballaje(self,caballaje):
       self.__caballaje=caballaje

   def getPlazas(self):
       return self.__plazas
    
   def setPlazas(self,plazas):
       self.__plazas=plazas

    #Metodoss o acciones o funciones que hace el objeto
   def acelerar(self):
      return "Estas acelerando"

   def frenar(self):
      return "Estas frenando"

#Fin definir clase

#Crear un objetos o instanciar la clase


class otra:
    pass