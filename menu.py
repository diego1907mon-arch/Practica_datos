from persona import Persona

lista_personas = []

def menu():
    while True:
        print("---- MENÚ PERSONAS ----")
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

            print("Persona registrada.")

        elif opcion == "2":
            if not lista_personas:
                print("No hay personas registradas.")
            else:
                print("--- LISTADO DE PERSONAS ---")
                for persona in lista_personas:
                    persona.mostrarDatos()

        elif opcion == "3":
            ced = input("Ingrese la cédula a buscar: ")

            for persona in lista_personas:
                if persona.cedula == ced:
                    print("Persona encontrada:")
                    persona.mostrarDatos()
                    break
            else:
                print("No existe una persona con esa cédula.")

        elif opcion == "4":
            print("Saliendo.")
            break

menu()