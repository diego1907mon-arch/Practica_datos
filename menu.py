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

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            correo = input("Correo: ")
            cedula = input("Cédula: ")

            persona = Persona(nombre, apellido, edad, correo, cedula)
            lista_personas.append(persona)

            print(" Persona registrada.")

        elif opcion == "2":
            if not lista_personas:
                print("No hay personas registradas.")
            else:
                print("--- LISTADO DE PERSONAS ---")
                for persona in lista_personas:
                    persona.mostrarDatos()