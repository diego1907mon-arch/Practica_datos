class Persona:  # Define la clase Persona
    def __init__(self, nombre, apellido, edad, correo, cedula):
        self.nombre = nombre       # Guarda el nombre en el atributo de la instancia
        self.apellido = apellido   # Guarda el apellido
        self.edad = edad           # Guarda la edad
        self.correo = correo       # Guarda el correo
        self.cedula = cedula       # Guarda la cédula

    def mostrarDatos(self):  # Método para imprimir los datos de la persona
        print("\n--- DATOS DE LA PERSONA ---")  # Encabezado
        print("Nombre:", self.nombre)            # Imprime el nombre
        print("Apellido:", self.apellido)        # Imprime el apellido
        print("Edad:", self.edad)                # Imprime la edad
        print("Correo:", self.correo)            # Imprime el correo
        print("Cédula:", self.cedula)            # Imprime la cédula

    def actualizarDatos(self, nombre=None, apellido=None, edad=None, correo=None):
        # Actualiza el nombre solo si se envía un valor
        if nombre:
            self.nombre = nombre

        # Actualiza el apellido solo si se envía un valor
        if apellido:
            self.apellido = apellido

        # Actualiza la edad solo si se envía un valor
        if edad:
            self.edad = edad

        # Actualiza el correo solo si se envía un valor
        if correo:
            self.correo = correo
