from persona import Persona

lista_personas = []

def menu():
    while True:
        print("\n---- MENÚ PERSONAS ----")
        print("1. Registrar persona")
        print("2. Mostrar todas las personas")
        print("3. Consultar persona por cédula")
        print("4. Editar persona por cédula")
        print("5. Eliminar persona por cédula")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        # Registrar persona
        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            correo = input("Correo: ")
            cedula = input("Cédula: ")

            persona = Persona(nombre, apellido, edad, correo, cedula)
            lista_personas.append(persona)

            print("Persona registrada.")

        # Mostrar todas las personas
        elif opcion == "2":
            if not lista_personas:
                print("No hay personas registradas.")
            else:
                print("\n--- LISTADO DE PERSONAS ---")
                for persona in lista_personas:
                    persona.mostrarDatos()

        # Consultar persona por cédula
        elif opcion == "3":
            ced = input("Ingrese la cédula a buscar: ")

            for persona in lista_personas:
                if persona.cedula == ced:
                    print("Persona encontrada:")
                    persona.mostrarDatos()
                    break
            else:
                print("No existe una persona con esa cédula.")

        # Editar persona por cédula
        elif opcion == "4":
            ced = input("Ingrese la cédula de la persona a editar: ")

            for persona in lista_personas:
                if persona.cedula == ced:
                    print("Persona encontrada. Deje un campo vacío para no modificarlo.")

                    nuevo_nombre = input(f"Nombre ({persona.nombre}): ")
                    nuevo_apellido = input(f"Apellido ({persona.apellido}): ")
                    nuevo_edad = input(f"Edad ({persona.edad}): ")
                    nuevo_correo = input(f"Correo ({persona.correo}): ")

                    # Actualiza solo lo que el usuario ingrese
                    persona.actualizarDatos(
                        nombre = nuevo_nombre or None,
                        apellido = nuevo_apellido or None,
                        edad = nuevo_edad or None,
                        correo = nuevo_correo or None
                    )

                    print("Datos actualizados correctamente.")
                    break
            else:
                print("No existe una persona con esa cédula.")
