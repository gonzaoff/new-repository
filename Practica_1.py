from abc import ABC, abstractmethod

#Quiero hacer un software que me diga donde se encuentra
#determinada palabra y de ser necesario la modifique.

#En el texto, buscar o reemplazar.
class pantalla(ABC):
    print("""
        Determine que desea realizar
        1. Buscar en el texto.
        2. Modificar en el texto.
        """)

#Seleccionar opcion.
class seleccionador(pantalla):
    @abstractmethod
    def seleccionador():
        pass

class Seleccion1(seleccionador):
    def selec1(self):
        #Informacion a tener en cuenta.
        print("ingrese el texto.")
        i = input()
        #Ingresa lo que quiere encontrar en el texto.
        print("¿Que palabra o conjuntos de palabras busca?")
        buscador = input()
        #Busca en el texto
        buscador_en_texto = i.find(buscador)
        #Almacena coincidencias del buscador
        coincidencias = i.count(buscador)
        #Si encuentra la palabra o frase, muestra su ubicacion
        if buscador_en_texto > -1:
            print(f"La palabra que busca se encuentra en el espacio {buscador_en_texto} y se repite {coincidencias} vez/ces.")
        #Sino encuentra la palabra o frase, niega.
        else:
            print("La frase o palabra no se encuentra en el texto.")

class Seleccion2(Seleccion1):
    def selec2(self):
    #Informacion a tener en cuenta.
        print("Ingrese el texto.")
        i = input()
        #Ingresa lo que quiere encontrar en el texto.
        print("Escriba la linea que desea cambiar")
        palabras_a_mod = input()
        busqueda_palabras = i.find(palabras_a_mod)
        coincidencias = i.count(palabras_a_mod)
        #Si lo encuentra, pide la modificacion.
        if busqueda_palabras > -1:
            print(f"la frase/palabra que buscas se encuentra {coincidencias} veces")
            print("escriba la modificacion a continuacion:")
            palabra_mod = input()
            reemplazo = i.replace(palabras_a_mod, palabra_mod)
            #imprime resultado
            print(f"""Su texto quedaria de la siguiente manera:
            {reemplazo}
                            """)
            #Sino existe, imprime...
        else:
            print("la palabra o frase no existe.")
#Acciones por buscar.
class BuscadorYModificador(Seleccion2):
    def seleccionador(self):
        select = int(input("Seleccione aqui: "))
        if select == 1:
            self.selec1()
        elif select == 2:
            self.selec2()
        else:
            print("la opcion seleccionada no existe.")
            


BusDePala=BuscadorYModificador()
BusDePala.seleccionador()