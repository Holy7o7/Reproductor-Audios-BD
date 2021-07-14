import folium

from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['FuentesSonorasAmbientales']

coleccion1 = baseDatos['archivos']

mapa = folium.Map(location =[-39.823641, -73.226158], zoom_start = 14)

for doc in coleccion1.find():
    latitud = doc['latitud']
    longitud = doc['longitud']
    fecha = doc['fecha_de_grabacion']
    folium.Marker([latitud,longitud], popup = fecha, tooltip = fecha).add_to(mapa)

###Debe cambiar la ruta!!!###
mapa.save('D:\\U\\7mo semestre\\Base de datos\\tarea\\mapa.html')

print("Mapa creado!")
