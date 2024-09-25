import ejercicio1
def calcula_estado_nutricional(peso, altura):
    imc = ejercicio1.calcula_imc(peso, altura)
    if imc < 18.5:
        estado = "bajo peso"
    elif imc < 25:
        estado = "Normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else :
        estado = "Obesidad"
    return estado


if __name__ == '__main__':     
    peso = float(input("introduzca el peso en kg:") )
    altura = float(input("introduzca la alura en m:"))
    imc = ejercicio1.calcula_imc(peso, altura)
    estado = calcula_estado_nutricional(peso, altura)
    print ( "El imc es :",  imc)
    print ( "El estado nutricional es :",  estado)
