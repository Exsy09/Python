def toDecimal(binario):
    try:
        decimal = int(binario, 2)
        valor = decimal
    except ValueError:
        decimal = -1
    return decimal





print(toDecimal("10110"))
print(toDecimal("345"))
print(toDecimal("hola"))