from Personaje import *

#1.Solicitar datos
print("")
print("####### Datos Heroe #")
especieH=input("Escribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH=float(input("Escribe la altura del Heroe: "))
recargarH=int(input("Cuantas balas recarga el Heroe: "))

print("")
print("####### Datos Villano #")
especieV=input("Escribe la especie del villano: ")
nombreV=input("Escribe el nombre del villano: ")
alturaV=float(input("Escribe la altura del villano: "))
recargarV=int(input("Cuantas balas recarga el villano: "))

#2. Crear objeto de clase personaje
heroe=Personaje(especieH,nombreH,alturaH)
villano=Personaje(especieV,nombreV,alturaV)

#3. Usar atributos
print("")
print("####### Objeto Heroe ####")
print("El personaje se llama: " + heroe.nombre)
print("Pertenece a la especie : " + heroe.especie)
print("Tiene una altura de: " + str(heroe.altura))
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargarH)

print("")
print("####### Objeto Villano ####")
print("El personaje se llama: " + villano.nombre)
print("Pertenece a la especie : " + villano.especie)
print("Tiene una altura de: " + str(villano.altura))
villano.correr(True)
villano.lanzarGranadas()
villano.recargarArma(recargarV)


