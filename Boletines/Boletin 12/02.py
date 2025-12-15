from abc import ABC, abstractmethod
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
    ROJO = "Rojo"


# =========================
# CLASE ABSTRACTA NOTA
# =========================

class Nota(ABC):
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now()

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def es_urgente(self):
        pass


# =========================
# CLASE NOTA NORMAL
# =========================

class NotaNormal(Nota):
    def __init__(self, titulo, descripcion, color):
        super().__init__(titulo, descripcion)
        self.color = color

    def es_urgente(self):
        return False

    def mostrar(self):
        return (
            f"📌 {self.titulo}\n"
            f"   {self.descripcion}\n"
            f"   Color: {self.color.value}\n"
            f"   Creada: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M')}\n"
        )


# =========================
# CLASE NOTA URGENTE
# =========================

class NotaUrgente(Nota):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)
        self.color = Color.ROJO

    def es_urgente(self):
        return True

    def mostrar(self):
        return (
            f"🚨🚨 NOTA URGENTE 🚨🚨\n"
            f"🔥 {self.titulo.upper()}\n"
            f"   {self.descripcion}\n"
            f"   Color: {self.color.value}\n"
            f"   Creada: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M')}\n"
            f"{'-'*35}\n"
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
                if nota.es_urgente():
                    confirmacion = input(
                        f"⚠️ La nota '{titulo}' es URGENTE. ¿Eliminar? (s/n): "
                    )
                    if confirmacion.lower() != "s":
                        print("❌ Eliminación cancelada.")
                        return
                self.notas.remove(nota)
                print(f"✅ Nota '{titulo}' eliminada.")
                return
        print(f"❌ No existe ninguna nota con título '{titulo}'.")

    def listarNotas(self):
        print("\n======= LISTA DE NOTAS =======\n")

        notas_urgentes = [n for n in self.notas if n.es_urgente()]
        notas_normales = [n for n in self.notas if not n.es_urgente()]

        for nota in notas_urgentes + notas_normales:
            print(nota.mostrar())


# =========================
# PRUEBA DEL PROGRAMA
# =========================

if __name__ == "__main__":
    gestor = GestorNotas()

    n1 = NotaNormal("Comprar pan", "Ir a la panadería", Color.AMARILLO)
    n2 = NotaNormal("Estudiar Python", "Repasar herencia", Color.VERDE)
    n3 = NotaUrgente("EXAMEN MAÑANA", "Estudiar POO")

    gestor.crearNota(n1)
    gestor.crearNota(n2)
    gestor.crearNota(n3)

    gestor.listarNotas()
    gestor.eliminarNota("EXAMEN MAÑANA")
    gestor.listarNotas()
