"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import csv

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog ():

    catalog = {"Sightings": None
    }

    catalog["Sightings"] = lt.newList("ARRAY_LIST")

    return catalog

# Funciones para agregar informacion al catalogo
def loadSightings(catalog):

    artworksfiles = cf.data_dir + "UFOS-utf8-small.csv"
    input_file = csv.DictReader(open(artworksfiles, encoding="utf-8"))
    for sighting in input_file:
        addSighting(catalog, sighting)

    prim5ult5 = lt.newList("ARRAY_LIST")

    for i in range(1, lt.size(catalog["Sightings"])+1):
        sight = lt.getElement(catalog["Sightings"], i)
        if i < 5:
            lt.addLast(prim5ult5, sight)
        elif i>=(lt.size(catalog["Sightings"])-5):
            lt.addLast(prim5ult5, sight)
    
    return prim5ult5

                


# Funciones para creacion de datos

def addSighting(catalog, sighting):

    lt.addLast(catalog["Sightings"], sighting)

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
