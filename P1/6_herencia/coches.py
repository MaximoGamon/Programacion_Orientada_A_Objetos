import os
os.system("cls")

class Coches:
    #atributos protegidos
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
       self._marca=marca
       self._color=color
       self._modelo=modelo
       self._velocidad=velocidad
       self._caballaje=caballaje
       self._plazas=plazas

    #1er Forma
   def getMarca(self):
       return self._marca
    
   def setMarca(self,marca):
       self._marca=marca

    #2da forma
   @property
   def marca2(self):
      return self._marca
    
   @marca2.setter
   def marca2(self,marca):
       self._marca=marca=marca

   def getColor(self):
       return self._color
    
   def setColor(self,color):
       self._color=color

   def getModelo(self):
       return self._modelo
    
   def setModelo(self,modelo):
       self._modelo=modelo

   def getVelocidad(self):
       return self._velocidad
    
   def setVelocidad(self,velocidad):
       self._velocidad=velocidad

   def getCaballaje(self):
       return self._caballaje
    
   def setCaballaje(self,caballaje):
       self._caballaje=caballaje

   def getPlazas(self):
       return self._plazas
    
   def setPlazas(self,plazas):
       self._plazas=plazas

    #Metodoss o acciones o funciones que hace el objeto
   def acelerar(self):
      return "Estas acelerando el coche"

   def frenar(self):
      return "Estas frenando frenando el coche"

#Fin definir clase

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga
    
    def acelerar(self):
        return "Estas acelerando el camion"
    
    def frenar(self):
        return "Estas frenando el camion"

    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje(self,eje):
        self.__eje=eje


    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    
    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga = capacidadCarga

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion = traccion
        self.__cerrada = cerrada

    def transportar(self,num_pasajero):
        self.num_pasajero=num_pasajero
        return self.num_pasajero
    
    def acelerar(self):
        return "Estas acelerando la camioneta"
    
    def frenar(self):
        return "Estas frenando la camioneta"
    
    @property
    def traccion(self):
        return self.__traccion
    
    @traccion.setter
    def traccion(self,tracccion):
        self.__traccion=tracccion


    @property
    def cerrrada(self):
        return self.__cerrada
    
    @cerrrada.setter
    def cerrada(self,cerrada):
        self.__cerrada=cerrada

        
