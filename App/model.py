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
from datetime import datetime
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def createCatalog():
  catalog = {
    'ufos': None,
    'datetime': None,
    'cities': None,
    'duration': None,
    'time': None,
    'coordinates': None,
  }

  catalog['ufos'] = lt.newList(datastructure='SINGLE_LINKED')
  catalog['cities'] = om.newMap(omaptype='RBT')
  catalog['duration'] = om.newMap(omaptype='RBT')
  catalog['time'] = om.newMap(omaptype='RBT')
  catalog['date'] = om.newMap(omaptype='RBT')
  catalog['coordinate'] = om.newMap(omaptype='RBT')

  return catalog

# Funciones para agregar informacion al catalogo

def newSighting(catalog, sighting):
  addByCity(catalog, sighting)
  addByDate(catalog, sighting)
  addByCoordinates(catalog, sighting)

# Funciones para creacion de datos

def addByCity(catalog, sighting):
  existingCity = om.get(catalog['cities'], sighting['city'])

  if existingCity is None:
    citiesLst = lt.newList()
    lt.addLast(citiesLst, sighting)
    om.put(catalog['cities'], sighting['city'], {
      'city': sighting['city'],
      'sightings': citiesLst,
    })
  else:
    citiesLst = me.getValue(existingCity)
    lt.addLast(citiesLst['sightings'], sighting)





def addByDate(catalog, sighting):
  existingDate = om.get(catalog['date'], datetime.strptime(sighting['datetime'], '%Y-%m-%d %H:%M:%S').date())

  if existingDate is None:
    dateLst = lt.newList()
    lt.addLast(dateLst, sighting)
    om.put(catalog['date'], datetime.strptime(sighting['datetime'], '%Y-%m-%d %H:%M:%S').date(), {
      'date': sighting['datetime'].split(' ')[0],
      'sightings': dateLst,
    })
  else:
    dateLst = me.getValue(existingDate)
    lt.addLast(dateLst['sightings'], sighting)


def addByCoordinates(catalog, sighting):
  existingCoordinate = om.get(catalog['coordinate'], round(float(sighting['longitude']), 2))

  if existingCoordinate is None:
    coordinateMap = om.newMap(omaptype='RBT')
    latitudesLst = lt.newList()
    lt.addLast(latitudesLst, sighting)
    om.put(coordinateMap, round(float(sighting['latitude']), 2), {
      'coordinate': sighting['latitude'],
      'sightings': latitudesLst,
    })
    om.put(catalog['coordinate'], round(float(sighting['longitude']), 2), {
      'coordinate': sighting['longitude'],
      'latitudes': coordinateMap,
    })
  else:
    coordinateMap = me.getValue(existingCoordinate)
    existingLatitude = om.get(coordinateMap['latitudes'], round(float(sighting['latitude']), 2))

    if existingLatitude is None:
      latitudesLst = lt.newList()
      lt.addLast(latitudesLst, sighting)
      om.put(coordinateMap['latitudes'], round(float(sighting['latitude']), 2), {
        'coordinate': sighting['latitude'],
        'sightings': latitudesLst,
      })
    else:
      latitudesLst = me.getValue(existingLatitude)
      lt.addLast(latitudesLst['sightings'], sighting)



# Funciones de consulta



def sightingsByCity(catalog, city):
  sightingsInCity = om.get(catalog['cities'], city)

  allCities = om.valueSet(catalog['cities'])
  
  sa.sort(me.getValue(sightingsInCity)['sightings'], sortByDatetime)

  sa.sort(allCities, sortBySize)

  return [me.getValue(sightingsInCity), allCities]



def sightingsSortedByDuration(catalog, minDuration, maxDuration):
  durationsInRange = om.values(catalog['duration'], minDuration, maxDuration)

  sightingsInRange = lt.newList('ARRAY_LIST')

  for lst in lt.iterator(durationsInRange):
    for sighting in lt.iterator(lst['sightings']):
      lt.addLast(sightingsInRange, sighting)

  allDurations = om.valueSet(catalog['duration'])

  sa.sort(sightingsInRange, sortByDatetime)

  return [allDurations, sightingsInRange]


def sightingsSortedByTime(catalog, minTime, maxTime):
  timeInRange = om.values(catalog['time'], minTime, maxTime)

  sightingsInRange = lt.newList('ARRAY_LIST')

  for lst in lt.iterator(timeInRange):
    for sighting in lt.iterator(lst['sightings']):
      lt.addLast(sightingsInRange, sighting)

  allTimes = om.valueSet(catalog['time'])

  sa.sort(sightingsInRange, sortByDatetime)

  return [allTimes, sightingsInRange]


def sightingsSortedByDate(catalog, minDate, maxDate):
  dateInRange = om.values(catalog['date'], minDate, maxDate)

  sightingsInRange = lt.newList('ARRAY_LIST')

  for lst in lt.iterator(dateInRange):
    for sighting in lt.iterator(lst['sightings']):
      lt.addLast(sightingsInRange, sighting)

  allDates = om.valueSet(catalog['date'])

  sa.sort(sightingsInRange, sortByDatetime)

  return [allDates, sightingsInRange]


def sightingsSortedByCoordinate(catalog, minLatitude, maxLatitude, minLongitude, maxLongitude, sort):
  coordinatesInRange = om.values(catalog['coordinate'], minLongitude, maxLongitude)

  sightingsInRange = lt.newList('ARRAY_LIST')

  for longitudes in lt.iterator(coordinatesInRange):
    for latitudes in lt.iterator(om.values(longitudes['latitudes'], minLatitude, maxLatitude)):
      for sighting in lt.iterator(latitudes['sightings']):
        lt.addLast(sightingsInRange, sighting)

  if sort:
    sightingsInRange = sa.sort(sightingsInRange, sortByDatetime)
  else:
    sightingsInRange = sa.sort(sightingsInRange, sortByCoordinates)

  return sightingsInRange

# Funciones de ordenamiento

def sortByDatetime(sighting_1, sighting_2):
  return datetime.strptime(sighting_1['datetime'], '%Y-%m-%d %H:%M:%S').date() < datetime.strptime(sighting_2['datetime'], '%Y-%m-%d %H:%M:%S').date()


def sortByCoordinates(sighting_1, sighting_2):
  if sighting_1['latitude'] > sighting_2['latitude']:
    return True
  elif sighting_1['longitude'] > sighting_2['longitude']:
    return True
  else:
    return False


def sortBySize(sighting_1, sighting_2):
  return lt.size(sighting_1['sightings']) > lt.size(sighting_2['sightings'])


def sort(lst):
  sa.sort(lst, sortByCount)
  return lst

def sortByCount(one, two):
  return lt.size(one['sightings']) < lt.size(two['sightings'])
  

def sortL(lst):
  sa.sort(lst, sortByLate)
  return lst

def sortByLate(one, two):
  return datetime.strptime(one['time'], '%H:%M:%S').time() > datetime.strptime(two['time'], '%H:%M:%S').time()


def sortD(lst):
  sa.sort(lst, sortByDate)
  return lst

def sortByDate(one, two):
  return datetime.strptime(one['date'], '%Y-%m-%d').date() < datetime.strptime(two['date'], '%Y-%m-%d').date()
