import os
os.system("cls")


class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    def inscribirse(self):
        pass

    def estudiar(self):
        pass
 
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_matricula(self):
        return self.__matricula




class Profesores:
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    def impartir(self):
        pass

    def evaluar(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_experiencia(self):
        return self.__experiencia
    
    def get_num_profesor(self):
        return self.__num_profesor
    



class Cursos:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def asignar(self):
        pass

    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo
    
    def get_creditos(self):
        return self.__creditos
    


Alumno1 = Alumnos("Maximo","19","1234567890")
Alumno2 = Alumnos("Eduardo","18","098754321")

print(f"Alumno 1: \n Nombre: {Alumno1.get_nombre()} \n Edad: {Alumno1.get_edad()} \n Matricula: {Alumno1.get_matricula() } \n Alumno 2: \n Nombre: {Alumno2.get_nombre()} \n Edad: {Alumno2.get_edad()} \n Matricula:{Alumno2.get_matricula() }")

Profesor1 = Profesores("Edgar","9","6181234567")
Profesor2 = Profesores("Alan","20","6180987654")

print(f"Profesor 1: \n Nombre: {Profesor1.get_nombre()} \n Experiencia: {Profesor1.get_experiencia()} \n Numero: {Profesor1.get_num_profesor() } \n Profesor 2: \n Nombre: {Profesor2.get_nombre()} \n Experiencia: {Profesor2.get_experiencia()} \n Numero: {Profesor2.get_num_profesor() }")

Curso1 = Cursos("Matemáticas", "1244198", 8)
Curso2 = Cursos("Inglés", "9091039", 9)
print(f"Curso 1: \n Nombre: {Curso1.get_nombre()} \n Codigo: {Curso1.get_codigo()} \n Creditos: {Curso1.get_creditos() } \n Curso 2: \n Nombre: {Curso2.get_nombre()} \n Codigo: {Curso2.get_codigo()} \n Creditos: {Curso2.get_creditos() }")

#asociacion profe cursos = imparte
#asociacion alumnos curso  = asiste