﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Inicializar catalogo")
    print("1- Contar avistamientos en una ciudad")
    print("2- Contar avistamientos por duracion")
    print("3- Contar Avistamientos por Hora/Minutos al dia")
    print("4- Contar avistaientos en rango de fecha")
    print("5- Contar avistamientos de una Zona Geografica")
    print("6- Contar Avistamientos por Hora/Minutos al dia")

def initCatalog():

    return controller.initCatalog()

def loadSightings(catalog):

    resultado = controller.loadSightings(catalog)

    return resultado

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        
        catalog = initCatalog()

        x = controller.loadSightings(catalog)
        print("Avistamientos cargados correctamente")
        print("''''''''''''''''''''''''''''''''''''''''''")
        print("Los primeros y ultimos 5 avistamientos son:")
        print("\n")
        for i in x['elements']:
            print(i)

    elif int(inputs[0]) == 1:
        x = 1
        print(x)

    else:
        sys.exit(0)
sys.exit(0)
