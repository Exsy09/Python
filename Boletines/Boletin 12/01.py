from datetime import datetime
from enum import Enum


# =========================
# ENUMERACIÓN DE COLORES
# =========================

class Color(Enum):
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    BLANCO = "Blanco"
    CYAN = "Cyan"


# =========================
# CLASE NOTA
# =========================

class Nota:
    def __init__(self, titulo, descripcion, color):
        self.titulo = titulo
        self.descripcion = descripcion
        self.color = color
        self.fecha_creacion = datetime.now()

    def mostrar(self):
        return (
            f"📌 {self.titulo}\n"
            f"   {self.descripcion}\n"
            f"   Color: {self.color.value}\n"
            f"   Creada: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M')}\n"
        )


# =========================
# CLASE GESTOR DE NOTAS
# =========================

class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNota(self, nota):
        self.notas.append(nota)

    def eliminarNota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                self.notas.remove(nota)
                print(f"✅ Nota '{titulo}' eliminada.")
                return
        print(f"❌ No existe ninguna nota con título '{titulo}'.")

    def listarNotas(self):
        print("\n======= LISTA DE NOTAS =======\n")
        for nota in self.notas:
            print(nota.mostrar())


# =========================
# PRUEBA DEL PROGRAMA
# =========================

if __name__ == "__main__":
    gestor = GestorNotas()

    nota1 = Nota("Comprar pan", "Ir a la panadería", Color.AMARILLO)
    nota2 = Nota("Estudiar Python", "Repasar clases y objetos", Color.VERDE)

    gestor.crearNota(nota1)
    gestor.crearNota(nota2)

    gestor.listarNotas()
    gestor.eliminarNota("Comprar pan")
    gestor.listarNotas()
