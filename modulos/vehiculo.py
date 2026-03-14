class vehiculo:

    def __init__(self, marca, modelo, anio, dueno=None):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__dueno = dueno   # asociacion

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_anio(self):
        return self.__anio

    def set_anio(self, anio):
        self.__anio = anio

    def get_dueno(self):
        return self.__dueno

    def set_dueno(self, dueno):
        self.__dueno = dueno

    def __len__(self):
        return len(self.__marca)

    def __str__(self):
        if self.__dueno:
            dueno = self.__dueno.get_nombre()
        else:
            dueno = "sin dueño"

        return f"marca: {self.__marca}\nmodelo: {self.__modelo}\nanio: {self.__anio}\ndueno: {dueno}"
