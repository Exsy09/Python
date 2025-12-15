from abc import ABC, abstractmethod
from enum import Enum


# =========================
# ENUMERACIONES
# =========================

class Departamento(Enum):
    INFORMATICA = "Informática"
    EMPRESA = "Empresa"
    INGLES = "Inglés"


class Grado(Enum):
    MEDIO = "Grado Medio"
    SUPERIOR = "Grado Superior"


class Curso(Enum):
    PRIMERO = 1
    SEGUNDO = 2


# =========================
# CLASE ABSTRACTA PERSONA
# =========================

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def mostrar_info(self):
        pass


# =========================
# CLASE ALUMNO
# =========================

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo, grupo):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.ciclo = ciclo
        self.grupo = grupo
        self.mayor_edad = self.edad >= 18

    def mostrar_info(self):
        return (f"Alumno: {self.nombre} {self.apellido}, "
                f"Edad: {self.edad}, Mayor de edad: {self.mayor_edad}, "
                f"Ciclo: {self.ciclo.nombre}, Grupo: {self.grupo.nombre}")


# =========================
# CLASE PROFESOR
# =========================

class Profesor(Persona):
    def __init__(self, nombre, apellido, departamento, grupo_tutor=None):
        super().__init__(nombre, apellido)
        self.departamento = departamento
        self.grupo_tutor = grupo_tutor

    def mostrar_info(self):
        tutor = self.grupo_tutor.nombre if self.grupo_tutor else "Ninguno"
        return (f"Profesor: {self.nombre} {self.apellido}, "
                f"Departamento: {self.departamento.value}, "
                f"Grupo tutor: {tutor}")


# =========================
# CLASE MODULO
# =========================

class Modulo:
    def __init__(self, nombre, segundo_curso, horas_semanales, optativo):
        self.nombre = nombre
        self.segundo_curso = segundo_curso
        self.horas_semanales = horas_semanales
        self.optativo = optativo

    def __str__(self):
        curso = "Segundo" if self.segundo_curso else "Primero"
        tipo = "Optativo" if self.optativo else "Obligatorio"
        return f"{self.nombre} ({curso}, {self.horas_semanales}h, {tipo})"


# =========================
# CLASE CICLO
# =========================

class Ciclo:
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado
        self.modulos = []

    def añadir_modulo(self, modulo):
        self.modulos.append(modulo)

    def __str__(self):
        return f"{self.nombre} - {self.grado.value}"


# =========================
# CLASE GRUPO
# =========================

class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor=None):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso
        self.tutor = tutor
        self.alumnos = []

    @property
    def numero_alumnos(self):
        return len(self.alumnos)

    def matricular_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        return [alumno.mostrar_info() for alumno in self.alumnos]

    def __str__(self):
        tutor = self.tutor.nombre if self.tutor else "Sin tutor"
        return (f"Grupo {self.nombre}, "
                f"Ciclo: {self.ciclo.nombre}, "
                f"Curso: {self.curso.name}, "
                f"Tutor: {tutor}, "
                f"Alumnos: {self.numero_alumnos}")


# =========================
# EJEMPLO DE USO
# =========================

if __name__ == "__main__":
    # Crear ciclo
    dam = Ciclo("Desarrollo de Aplicaciones Multiplataforma", Grado.SUPERIOR)

    # Crear módulos
    prog = Modulo("Programación", False, 8, False)
    bbdd = Modulo("Bases de Datos", False, 6, False)

    dam.añadir_modulo(prog)
    dam.añadir_modulo(bbdd)

    # Crear profesor
    profesor = Profesor("Ana", "López", Departamento.INFORMATICA)

    # Crear grupo
    grupo_dam1 = Grupo("DAM1", dam, Curso.PRIMERO, profesor)
    profesor.grupo_tutor = grupo_dam1

    # Crear alumnos
    alumno1 = Alumno("Carlos", "Pérez", 19, dam, grupo_dam1)
    alumno2 = Alumno("Lucía", "Gómez", 17, dam, grupo_dam1)

    grupo_dam1.matricular_alumno(alumno1)
    grupo_dam1.matricular_alumno(alumno2)

    # Mostrar información
    print(grupo_dam1)
    for info in grupo_dam1.mostrar_alumnos():
        print(info)
