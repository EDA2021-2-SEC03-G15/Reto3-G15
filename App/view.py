"""
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
import controller
from DISClib.ADT import list as lt
assert cf

def citiesBySightings(catalog):
    city = input('Ingresa la ciudad: ')

    info = controller.sightingByCity(catalog, city)

    print('Hay', lt.size(info[1]), 'ciudades con avistamientos reportados')
    print('El top 5 es:')
    print('\n')

    for city in lt.iterator(lt.subList(info[1], 1, 5)):
        print(city['city'], ':', lt.size(city['sightings']))
    
    print('\nHay', lt.size(info[0]['sightings']), 'avistamientos en la ciudad seleccionada.')
    print('Los primeros 3 y ultimos 3 avistamientos en la ciudad son: ')

    for sighting in lt.iterator(lt.subList(info[0]['sightings'], 1, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        
    for sighting in lt.iterator(lt.subList(info[0]['sightings'], lt.size(info[0]['sightings']) - 2, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])


def sightingsInDurationRange(catalog):
    minTime = input('Ingresa el tiempo minimo: ')
    maxTime = input('Ingresa el tiempo máximo: ')

    info = controller.sightingsByDurationRange(catalog, minTime, maxTime)

    print('Hay', lt.size(info[0]), 'diferentes duraciones.')
    print('El top 5 es:')
    print('\n')

    top5 = lt.subList(info[0], lt.size(info[0]) - 4, 5)
    
    sorted = controller.sortBySize(top5)

    for duration in lt.iterator(sorted):
        print(duration['duration'], ':', lt.size(duration['sightings']))
    
    print('\nHay', lt.size(info[1]), 'avistamientos en el rango seleccionado.')
    print('Los primeros 3 y ultimos 3 avistamientos en el rango son: ')

    for sighting in lt.iterator(lt.subList(info[1], 1, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        
    for sighting in lt.iterator(lt.subList(info[1], lt.size(info[1]) - 2, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])


def sightingsInTimeRange(catalog):
    minTime = input('Ingresa la hora minima: ')
    maxTime = input('Ingresa la hora máxima: ')

    info = controller.sightingsByTimeRange(catalog, minTime, maxTime)

    print('Hay', lt.size(info[0]), 'diferentes horas.')
    print('El top 5 más tardio es:')
    print('\n')

    top5 = lt.subList(info[0], lt.size(info[0]) - 4, 5)
    
    sorted = controller.sortByLate(top5)

    for duration in lt.iterator(sorted):
        print(duration['time'], ':', lt.size(duration['sightings']))
    
    print('\nHay', lt.size(info[1]), 'avistamientos en el rango seleccionado.')
    print('Los primeros 3 y ultimos 3 avistamientos en el rango son: ')

    for sighting in lt.iterator(lt.subList(info[1], 1, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        
    for sighting in lt.iterator(lt.subList(info[1], lt.size(info[1]) - 2, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])


def sightingsInDateRange(catalog):
    minTime = input('Ingresa la fecha minima: ')
    maxTime = input('Ingresa la fecha máxima: ')

    info = controller.sightingsByDateRange(catalog, minTime, maxTime)

    print('Hay', lt.size(info[0]), 'diferentes fechas.')
    print('El top 5 más antiguo es:')
    print('\n')

    top5 = lt.subList(info[0], 1, 5)
    
    sorted = controller.sortByDate(top5)

    for duration in lt.iterator(sorted):
        print(duration['date'], ':', lt.size(duration['sightings']))
    
    print('\nHay', lt.size(info[1]), 'avistamientos en el rango seleccionado.')
    print('Los primeros 3 y ultimos 3 avistamientos en el rango son: ')

    for sighting in lt.iterator(lt.subList(info[1], 1, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        
    for sighting in lt.iterator(lt.subList(info[1], lt.size(info[1]) - 2, 3)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])


def sightingsInCoordinateRange(catalog):
    minLatitude = input('Ingresa la latitud minima: ')
    maxLatitude = input('Ingresa la latitud maxima: ')
    minLongitude = input('Ingresa la longitud minima: ')
    maxLongitude = input('Ingresa la longitud maxima: ')

    info = controller.sightingsByCoordinateRange(catalog, minLatitude, maxLatitude, minLongitude, maxLongitude, True)

    print('Hay', lt.size(info), 'diferentes avistamientos en el area indicada.')
    print('\n')

    for sighting in lt.iterator(lt.subList(info, 1, 5)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        print('Latitud:', sighting['latitude'])
        print('Longitud:', sighting['longitude'])
        
    for sighting in lt.iterator(lt.subList(info, lt.size(info) - 4, 5)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        print('Latitud:', sighting['latitude'])
        print('Longitud:', sighting['longitude'])


def sightingsMapInCoordinateRange(catalog):
    minLatitude = input('Ingresa la latitud minima: ')
    maxLatitude = input('Ingresa la latitud maxima: ')
    minLongitude = input('Ingresa la longitud minima: ')
    maxLongitude = input('Ingresa la longitud maxima: ')

    info = controller.sightingsByCoordinateRange(catalog, minLatitude, maxLatitude, minLongitude, maxLongitude, False)

    print('Hay', lt.size(info), 'diferentes avistamientos en el area indicada.')
    print('\n')

    for sighting in lt.iterator(lt.subList(info, 1, 5)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        print('Latitud:', sighting['latitude'])
        print('Longitud:', sighting['longitude'])
        
    for sighting in lt.iterator(lt.subList(info, lt.size(info) - 4, 5)):
        print('\nFecha y hora:', sighting['datetime'])
        print('Ciudad:', sighting['city'])
        print('Estado:', sighting['state'])
        print('País:', sighting['country'])
        print('Duración(s):', sighting['duration (seconds)'])
        print('Forma:', sighting['shape'])
        print('Latitud:', sighting['latitude'])
        print('Longitud:', sighting['longitude'])


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una Zona Geográfica")
    print("7- Visualizar los avistamientos de una zona geográfica.")
    print("8- Salir")

catalog = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        catalog = controller.loadData(catalog, input('Ingresa el nombre del archivo que contiene la información: '))
    elif int(inputs[0]) == 2:
        citiesBySightings(catalog)
    elif int(inputs[0]) == 3:
        sightingsInDurationRange(catalog)
    elif int(inputs[0]) == 4:
        sightingsInTimeRange(catalog)
    elif int(inputs[0]) == 5:
        sightingsInDateRange(catalog)
    elif int(inputs[0]) == 6:
        sightingsInCoordinateRange(catalog)
    elif int(inputs[0]) == 7:
        sightingsMapInCoordinateRange(catalog)
    else:
        break