
def calcula_imc(peso, altura):
    return peso/ (altura * altura)

if __name__ == '__main__':     
    peso = float(input("introduzca el peso en kg:") )
    altura = float(input("introduzca la alura en m:"))
    imc = calcula_imc(peso, altura)
    print ( "El imc es :",  imc)