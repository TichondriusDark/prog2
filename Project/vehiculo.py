#CLASE PADRE
class Vehiculo:
    def __init__(self, marca, modelo, anio, color, kilometraje, TipoCombustible, patente):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.kilometraje = kilometraje
        self.TipoCombustible = TipoCombustible
        self.paptente = patente

    def encender(self):
        return print("Encendido")
    def apagar(self):
        return print("Apagado")
    def frenar(self):
        return print("Frenando...")
    
#CLASES HIJAS
class Auto(Vehiculo):
    def __init__(self, CantidadPuertas, TipoCarroceria, marca, modelo, anio, color, kilometraje, TipoCombustible, patente):
        super().__init__(marca, modelo, anio, color, kilometraje, TipoCombustible, patente)
        self.CantidadPuertas = CantidadPuertas
        self.TipoCarroceria = TipoCarroceria

    def Abrirbaul(self):
        return print("Baul Abierto")
    
    def Cerrarbaul(self):
        return print("Baul Cerrado")
    

class Camioneta(Vehiculo):
    def __init__(self, capacidad, CajaAbierta, marca, modelo, anio, color, kilometraje, TipoCombustible, patente):
        super().__init__(marca, modelo, anio, color, kilometraje, TipoCombustible, patente)
        self.capacidad = capacidad
        self.CajaAbierta = CajaAbierta

class Moto(Vehiculo):
    def __init__(self, cilindrada, marca, modelo, anio, color, kilometraje, TipoCombustible, patente):
        super().__init__(marca, modelo, anio, color, kilometraje, TipoCombustible, patente)
        self.cilindrada = cilindrada

    def Ponerpata(self):
        return print("Moto estacionada")
    
    def Quitarpata(self):
        return print("Lista para arrancar")
    
auto_uno = Auto(4, "SEDAN", "Honda", "Civic", "2021", "Negro", 100.000, "Nafta", "112ABC")
print(auto_uno.Abrirbaul())

camioneta_uno = Camioneta("1T", True, "Toyota", "HILUX", 2018, "Rojo", 80.000, "Diésel", "BB124")
print(camioneta_uno.encender())

moto_uno = Moto("471cc", "Honda", "CB 500X", 2020, "Blanco", 12.000, "Gasolina", "AD456")
print(moto_uno.Ponerpata())
