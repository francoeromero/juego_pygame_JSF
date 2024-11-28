from funciones import *

lista_datos = cargar_datos_json("puntajes.json")

print(lista_datos)

print("--------------")

print(quick_sort(lista_datos, 'puntuacion'))