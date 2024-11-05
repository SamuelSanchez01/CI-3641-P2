from functions import *

while True:
        userInput = input("Ingrese una accion: ").strip()
        if userInput.startswith("EVAL"):
            parts = userInput.split()
            order = parts[1]
            expression = ' '.join(parts[2:])
            if order == "PRE":
                print("Resultado:", evaluatePrefix(expression))
            elif order == "POST":
                print("Resultado:", evaluatePostfix(expression))
            else:
                print("Orden no reconocido. Use PRE o POST.")
        elif userInput.startswith("MOSTRAR"):
            parts = userInput.split()
            order = parts[1]
            expression = ' '.join(parts[2:])
            if order == "PRE":
                print("Mostrar: ", showPrefix(expression))
            elif order == "POST":
                print("Mostrar: ", showPostfix(expression))
            else:
                print("Orden no reconocido. Use PRE o POST.")
        elif userInput == "SALIR":
            exit(0)
        else:
            print("Accion no reconocida. Use EVAL, MOSTRAR o Salir")