
# Clase
class Profesor: 
   #Atributos
    def __init__(self, nombre: str, materia, curso):
      self.materia = materia
      self.nombre = nombre
      self.curso = curso
   #Metodos
    def saludar(self):
      return print(f"Hola Delvelopers, Me llamo {self.nombre}")      
      
      
profe_uno = Profesor("Pepe", "Programacion", "Prog2")

print(profe_uno.saludar())

profe_dos = Profesor("Ana", "base de datos", "Prog3")

print(profe_dos.saludar())
