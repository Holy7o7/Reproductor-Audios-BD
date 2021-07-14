from bson.binary import Binary
from bson import ObjectId
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['FuentesSonorasAmbientales']

coleccion2 = baseDatos['audios']

###El archivo de audio a ingresar debe estar en la misma ruta que este codigo###

audioHosp = 'hospital.wav'

with open(audioHosp, "rb") as f:
    encoded = Binary(f.read())
coleccion2.insert_one({"nombre_archivo": audioHosp, "file": encoded, "descripcion": "grabacion del interior de un hospital", "fecha_archivo": "25/12/1999"})

audioPob1 = 'poblacion1.wav'

with open(audioPob1, "rb") as f:
    encoded = Binary(f.read())
coleccion2.insert_one({"nombre_archivo": audioPob1, "file": encoded, "descripcion": "grabacion de una poblacion en el sector de las animas", "fecha_archivo": "21/09/2020" })

audiopobl2 = 'poblacion2.wav'

with open(audiopobl2, "rb") as f:
    encoded = Binary(f.read())
coleccion2.insert_one({"nombre_archivo": audiopobl2, "file": encoded, "descripcion": "grabacion de una pobblacion en el sector de isla teja", "fecha_archivo": "13/01/2021"})

print("Audios Ingresados")
