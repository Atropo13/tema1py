import ejercicio1
import ejercicio2
def imprime_estado_nutricional(pesos_y_alturas):
        for persona in pesos_y_alturas:
            imc = ejercicio1.calcula_imc(persona[0], persona[1])
            estado = ejercicio2.calcula_estado_nutricional(persona[0], persona[1])
            print("El IMC es", imc, "y su estado nutricional es", estado)
            
if __name__ == '__main__':
      personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
    ]
      imprime_estado_nutricional(personas)