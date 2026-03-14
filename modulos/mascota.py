class mascota:

    def __init__(self, nombre, especie, edad):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def __len__(self):
        return len(self.__nombre)

    def __str__(self):
        return f"nombre: {self.__nombre}\nespecie: {self.__especie}\nedad: {self.__edad}"
