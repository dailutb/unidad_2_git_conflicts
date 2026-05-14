# Importamos dependencias
from shared.utilities import sumar, restar


# Declaramos/inicializamos variables
num1 = 1
num2 = 3


# Declaramos la función main
def main():
    print("Calculadora en Python") 
    print(f"Los números son: {num1, num2}")
    print(f"La resta es: {restar(num1, num2)}")
    print(f"La suma es: {sumar(num1, num2)}")


if __name__ == "__main__":
    main()

