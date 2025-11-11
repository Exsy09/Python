import re

def matriculasValidas(* matriculas):
    contCorrecto = 0
    contIncorrecto = 0
    for matricula in matriculas:
        if re.fullmatch(r"\d{4}(-| )[A-Z][^AEIUO]{3}$", matricula):
            print(matricula, "es valida")
            contCorrecto += 1
        else:
            print(matricula, "no es valida")
            contIncorrecto += 1

    print("Matriculas validas: ", contCorrecto, "\nMatriculas no validas: ", contIncorrecto)

print(matriculasValidas("5432 - BFC", "3456BAC"))
