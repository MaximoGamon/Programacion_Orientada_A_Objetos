from conexionBD import *

class Estudiante:
    def __init__(self, nombre, nota, id=None):
        self._nombre = nombre
        self._nota = nota
        self.id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def imprimir(self):
        print(f"El alumno {self._nombre}, obtuvo una nota: {self._nota}")

    def mostrar_nota(self):
        if self._nota >= 7:
            print(f"La calificación de la nota es: {self._nota}. ✅ Ha aprobado.")
        else:
            print(f"La calificación de la nota es: {self._nota}. ❌ No ha aprobado.")

    def crear(self):
        try:
            cursor.execute(
                "INSERT INTO estudiantes (nombre, nota, fecha_registro) VALUES (%s, %s, NOW())",
                (self._nombre, self._nota)
            )
            conexion.commit()
            print("✅ Estudiante registrado correctamente.")
            return True
        except Exception as e:
            print("❌ Error al crear el estudiante:", e)
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute("SELECT * FROM estudiantes")
            estudiantes = cursor.fetchall()
            print("📋 Lista de estudiantes:")
            for est in estudiantes:
                print(est)
            return estudiantes
        except Exception as e:
            print("❌ Error al mostrar estudiantes:", e)
            return []

    def actualizar(self):
        try:
            cursor.execute(
                "UPDATE estudiantes SET nombre=%s, nota=%s WHERE id=%s",
                (self._nombre, self._nota, self.id)
            )
            conexion.commit()
            print("✅ Estudiante actualizado correctamente.")
            return True
        except Exception as e:
            print("❌ Error al actualizar estudiante:", e)
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM estudiantes WHERE id=%s", (id,))
            conexion.commit()
            print("🗑️ Estudiante eliminado correctamente.")
            return True
        except Exception as e:
            print("❌ Error al eliminar estudiante:", e)
            return False
