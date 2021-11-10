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

from datetime import datetime
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
  return model.createCatalog()

# Funciones para la carga de datos

def loadData(catalog, file):
  ufosfile = cf.data_dir + file
  input_file = csv.DictReader(open(ufosfile, encoding='utf-8'), delimiter=',')

  for ufo in input_file:
    model.newSighting(catalog, ufo)
  
  return catalog


def sightingByCity(catalog, city):
  return model.sightingsByCity(catalog, city)


def sightingsByDurationRange(catalog, minTime, maxTime):
  return model.sightingsSortedByDuration(catalog, float(minTime), float(maxTime))


def sightingsByTimeRange(catalog, minTime, maxTime):
  minTime = datetime.strptime(minTime + ':00', '%H:%M:%S').time()
  maxTime = datetime.strptime(maxTime + ':00', '%H:%M:%S').time()

  return model.sightingsSortedByTime(catalog, minTime, maxTime)


def sightingsByDateRange(catalog, minDate, maxDate):
  minDate = datetime.strptime(minDate, '%Y-%m-%d').date()
  maxDate = datetime.strptime(maxDate, '%Y-%m-%d').date()

  return model.sightingsSortedByDate(catalog, minDate, maxDate)


def sightingsByCoordinateRange(catalog, minLatitude, maxLatitude, minLongitude, maxLongitude, sort):
  minLatitude = float(minLatitude)
  maxLatitude = float(maxLatitude)
  minLongitude = float(minLongitude)
  maxLongitude = float(maxLongitude)

  return model.sightingsSortedByCoordinate(catalog, minLatitude, maxLatitude, minLongitude, maxLongitude, sort)

# Funciones de ordenamiento

def sortBySize(lst):
  return model.sort(lst) 

def sortByLate(lst):
  return model.sortL(lst) 

def sortByDate(lst):
  return model.sortD(lst) 