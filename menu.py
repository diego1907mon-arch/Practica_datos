from persona import Persona   # Importa la clase Persona desde persona.py

lista_personas = []  # Lista donde se guardarán los objetos Persona


def menu():  # Función principal del menú
    while True:  # Ciclo infinito para que el menú se repita
        print("\n---- MENÚ PERSONAS ----")       # Muestra el menú
        print("1. Registrar persona")            # Opción 1
        print("2. Mostrar todas las personas")   # Opción 2
        print("3. Consultar persona por cédula") # Opción 3
        print("4. Editar persona por cédula")    # Opción 4
        print("5. Eliminar persona por cédula")  # Opción 5
        print("6. Salir")                        # Opción 6

        opcion = input("Seleccione una opción: ")  # Captura la opción ingresada

        # ---- OPCIÓN 1: REGISTRAR PERSONA ----
        if opcion == "1":
            nombre = input("Nombre: ")        # Pide nombre
            apellido = input("Apellido: ")    # Pide apellido
            edad = input("Edad: ")            # Pide edad
            correo = input("Correo: ")        # Pide correo
            cedula = input("Cédula: ")        # Pide cédula

            # Crea un objeto Persona con los datos ingresados
            persona = Persona(nombre, apellido, edad, correo, cedula)
            lista_personas.append(persona)   # Lo agrega a la lista

            print("Persona registrada.")     # Confirmación

        # ---- OPCIÓN 2: MOSTRAR TODAS LAS PERSONAS ----
        elif opcion == "2":
            if not lista_personas:  # Si la lista está vacía
                print("No hay personas registradas.")
            else:
                print("\n--- LISTADO DE PERSONAS ---")
                for persona in lista_personas:  # Recorre cada persona
                    persona.mostrarDatos()      # Llama al método que imprime todo

        # ---- OPCIÓN 3: CONSULTAR PERSONA POR CÉDULA ----
        elif opcion == "3":
            ced = input("Ingrese la cédula a buscar: ")  # Pide cédula

            # Recorre la lista buscando coincidencia
            for persona in lista_personas:
                if persona.cedula == ced:  # Si la cédula coincide
                    print("Persona encontrada:")
                    persona.mostrarDatos()  # Muestra sus datos
                    break  # Deja de buscar
            else:
                # Este else pertenece al for: se ejecuta si NO se hizo break
                print("No existe una persona con esa cédula.")

        # ---- OPCIÓN 4: EDITAR PERSONA ----
        elif opcion == "4":
            ced = input("Ingrese la cédula de la persona a editar: ")

            # Buscar persona con esa cédula
            for persona in lista_personas:
                if persona.cedula == ced:
                    print("Persona encontrada. Deje un campo vacío para no modificarlo.")

                    # Muestra el valor actual entre paréntesis
                    nuevo_nombre = input(f"Nombre ({persona.nombre}): ")
                    nuevo_apellido = input(f"Apellido ({persona.apellido}): ")
                    nuevo_edad = input(f"Edad ({persona.edad}): ")
                    nuevo_correo = input(f"Correo ({persona.correo}): ")

                    # actualiza solo los campos que NO estén vacíos
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

        # ---- OPCIÓN 5: ELIMINAR PERSONA ----
        elif opcion == "5":
            ced = input("Ingrese la cédula de la persona a eliminar: ")

            # Busca en la lista
            for persona in lista_personas:
                if persona.cedula == ced:
                    lista_personas.remove(persona)  # Elimina la persona
                    print("Persona eliminada correctamente.")
                    break
            else:
                print("No existe una persona con esa cédula.")

        # ---- OPCIÓN 6: SALIR DEL PROGRAMA ----
        elif opcion == "6":
            print("Saliendo.")  # Mensaje de salida
            break  # Termina el ciclo, finalizando el menú

        # ---- OPCIÓN INVÁLIDA ----
        else:
            print("Opción no válida. Intente de nuevo.")  # Mensaje de error


menu()  # Llama la función para ejecutar el programa
