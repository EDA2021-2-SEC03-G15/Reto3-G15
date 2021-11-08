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
 """

import config as cf
import model
import csv
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros}
def initCatalog():

    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadSightings(catalog):

    return model.loadSightings(catalog)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def sightingSize(catalog):
    return model.sightingsSize(catalog)


def indexHeight(catalog):
    return model.indexHeight(catalog)


def indexSize(catalog):
    return model.indexSize(catalog)


def minKey(catalog):
    return model.minKey(catalog)


def maxKey(catalog):
    return model.maxKey(catalog)


def getSightingsByRange(catalog, initialDate, finalDate):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.getSightingsByRange(catalog, initialDate.date(), finalDate.date())


def getSightingsByCity(analyzer, city):
    return model.getSightingsByCity(analyzer, city)