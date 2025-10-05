from coches import *

#Solicitar datos queposteriormente seran los atributos del objeto

num_coches=int(input("¿Cuantos coches tienes?: "))

for i in range(0,num_coches):

    print(f"\n\t ... Datos del automovil  {i+1}...")
    marca=input("Ingresa la marca del auto:  ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("ingresa el modelo: ").upper()
    velocidad=int(input("Ingrese la velocidad: "))
    potencia=int(input("Imgrese la potencia: "))
    plazas=int(input("Ingrese el # de plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"\n\t Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()}  ")


#coche1=Coches("VW","Blanco","2022",220,150,5)
#coche2=Coches("Nissan","Azul","2020",180,150,6)
#coche3=Coches("Honda","","",0,0,0)
#coche1.num_serie="B014567890"
#coche4=Coches("","","",0,0,0)
#coche4.marca2="Volvo"
#print(coche4.marca2)

#print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} \n numero de serie: {coche1.num_serie} ")
#print(f"\nDatos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")

#print(coche3.marca2)