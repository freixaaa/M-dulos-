from persona import persona
from mascota import mascota
from vehiculo import vehiculo


personas = []
mascotas = []
vehiculos = []


def pedir_numero(mensaje):
    while True:
        print(mensaje)
        valor = input().strip()
        if valor.isdigit():
            return int(valor)
        else:
            print("ingrese un numero valido\n")


def crear_persona():
    print("nombre:")
    nombre = input().strip()

    edad = pedir_numero("edad:")

    print("profesion:")
    profesion = input().strip()

    personas.append(persona(nombre, edad, profesion))
    print("persona creada\n")


def crear_mascota():
    print("nombre:")
    nombre = input().strip()

    print("especie:")
    especie = input().strip()

    edad = pedir_numero("edad:")

    mascotas.append(mascota(nombre, especie, edad))
    print("mascota creada\n")


def crear_vehiculo():
    print("marca:")
    marca = input().strip()

    print("modelo:")
    modelo = input().strip()

    anio = pedir_numero("anio:")

    vehiculos.append(vehiculo(marca, modelo, anio))
    print("vehiculo creado\n")


def imprimir_lista(lista):
    if not lista:
        print("no hay registros\n")
    else:
        for obj in lista:
            print(obj)
            print()


def menu():
    while True:
        print("simulador de vida")
        print("1. crear persona")
        print("2. crear mascota")
        print("3. crear vehiculo")
        print("4. imprimir personas")
        print("5. imprimir mascotas")
        print("6. imprimir vehiculos")
        print("7. imprimir todas las entidades")
        print("8. salir")

        print("seleccione una opcion:")
        opcion = input().strip()

        if opcion == "8":
            break

        if not opcion.isdigit():
            print("ingrese un numero valido\n")
            continue

        opcion = int(opcion)

        if opcion == 1:
            crear_persona()
        elif opcion == 2:
            crear_mascota()
        elif opcion == 3:
            crear_vehiculo()
        elif opcion == 4:
            imprimir_lista(personas)
        elif opcion == 5:
            imprimir_lista(mascotas)
        elif opcion == 6:
            imprimir_lista(vehiculos)
        elif opcion == 7:
            imprimir_lista(personas)
            imprimir_lista(mascotas)
            imprimir_lista(vehiculos)
        else:
            print("opcion fuera de rango\n")


if __name__ == "__main__":
    menu()
