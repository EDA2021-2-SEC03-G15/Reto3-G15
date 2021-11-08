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
from DISClib.DataStructures import orderedmapstructure as om
import datetime
assert cf
import csv

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog ():

    catalog = {"Sightings": None,
                "CityIndex": None
    }

    catalog["Sightings"] = lt.newList("ARRAY_LIST")
    catalog["CityIndex"] = om.newMap(omaptype="RBT",
                                comparefunction=compareCity

    )

    return catalog

# Funciones para agregar informacion al catalogo
def loadSightings(catalog):

    artworksfiles = cf.data_dir + "UFOS-utf8-small.csv"
    input_file = csv.DictReader(open(artworksfiles, encoding="utf-8"))
    for sighting in input_file:
        addSighting(catalog, sighting)

    return catalog

# Funciones para creacion de datos


def addSighting(catalog, sighting):
    
    lt.addLast(catalog["Sightings"], sighting)
    updateCitySighting(catalog["CityIndex"], sighting)
    return catalog


def updateCitySighting(map, sighting):


    sightingCity = sighting['city']

    entry = om.get(map, sightingCity)
    if entry is None:
        datentry = newDataEntry(sighting)
        om.put(map, sightingCity, datentry)
    else:
        datentry = me.getValue(entry)
    addCityIndex(datentry, sighting)
    return map

def addCityIndex(datentry, sighting):


    lst = datentry['lstsighting']
    lt.addLast(lst, sighting)
    cityIndex = datentry['CityIndex']
    cityentry = mp.get(cityIndex, sighting['city'])
    if (cityentry is None):
        entry = newCityEntry(sighting['city'], sighting)
        lt.addLast(entry['lstcities'], sighting)
        mp.put(cityIndex, sighting['city'], entry)
    else:
        entry = me.getValue(cityentry)
        lt.addLast(entry['lstcities'], sighting)
    return datentry

def newDataEntry(sighting):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'CityIndex': None, 'lstsighting': None}
    entry['CityIndex'] = mp.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareCity)
    entry['lstsighting'] = lt.newList('SINGLE_LINKED', compareCity)
    return entry

def newCityEntry(citygrp, sighting):
    """
    Crea una entrada en el indice por ciudad, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    cityentry = {'city': None, 'lstcities': None}
    cityentry['city'] = citygrp
    cityentry['lstcities'] = lt.newList('SINGLELINKED', compareCity)
    return cityentry


# Funciones de consulta

def sightingSize(catalog):
    return lt.size(catalog['Sightings'])

def indexHeight(catalog):
    return om.height(catalog['CityIndex'])

def indexSize(catalog):
    return om.size(catalog['CityIndex'])

def minKey(catalog):
    return om.minKey(catalog['CityIndex']) 

def maxKey(catalog):
    return om.maxKey(catalog['CityIndex'])


def getSightingsByCity(catalog, city):

    sighdate = om.get(catalog['CityIndex'], city)
    if sighdate['key'] is not None:
        citymap = me.getValue(sighdate)['cityIndex']
        numcities = mp.get(citymap, city)
        if numcities is not None:
            return mp.size(me.getValue(numcities)['lstcities'])
    return 0  

# Funciones utilizadas para comparar elementos dentro de una lista

def compareCity(city1, city2):

    city = me.getKey(city2)
    if (city1 == city):
        return 0
    elif (city1 > city):
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
# Funciones de ordenamiento

