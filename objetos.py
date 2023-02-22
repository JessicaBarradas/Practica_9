from Personaje import *

#1.Solicitar datos
print("")
print("####### Datos Heroe #")
especieH=input("Escribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH=input("Escribe la altura del Heroe: ")
recargarH=input("Cuantas balas recarga el Heroe: ")

print("")
print("####### Datos Villano #")
especieV=input("Escribe la especie del villano: ")
nombreV=input("Escribe el nombre del villano: ")
alturaV=input("Escribe la altura del villano: ")
recargarV=input("Cuantas balas recarga el villano: ")


#1. Crear objeto de clase personaje
heroe= Personaje()
#2. Usar atributos
print("El personaje se llama: " + heroe.nombre)
print("Pertenece a la especie : " + heroe.especie)
print("Tiene una altura de: " + heroe.altura)
#3. Usar metodos
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(87)
