from persona import Persona

lista_personas = []

def menu():
    while True:
        print("===== MENÚ PERSONAS =====")
        print("1. Registrar persona")
        print("2. Mostrar todas las personas")
        print("3. Consultar persona por cédula")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")