class Persona:
    def __init__(self, nombre, apellido, edad, correo, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.cedula = cedula

    def mostrarDatos(self):
        print("--- DATOS DE LA PERSONA ---")
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)
        print("Correo:", self.correo)
        print("Cédula:", self.cedula)
