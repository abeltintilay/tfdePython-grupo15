'''

for i in range(3):
    print(i)


def saludar(nombre, signo = "!"):
    print(f'Hola {nombre}{signo}')

saludar("alumnos", "")


mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

del mi_diccionario['b']

print(mi_diccionario)

'''
mi_lista = [0, 1, 2, 3, 4, 5]

print(mi_lista[1:4])