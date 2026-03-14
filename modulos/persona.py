class persona:

    def __init__(self, nombre, edad, profesion):
        self.__nombre = nombre
        self.__edad = edad
        self.__profesion = profesion
        self.__mascotas = []   # composicion

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_profesion(self):
        return self.__profesion

    def set_profesion(self, profesion):
        self.__profesion = profesion

    def __len__(self):
        return len(self.__mascotas)

    def __str__(self):
        return f"nombre: {self.__nombre}\nedad: {self.__edad}\nprofesion: {self.__profesion}\nmascotas: {len(self.__mascotas)}"
