import playsound
from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['FuentesSonorasAmbientales']

coleccion2 = baseDatos['audios']

paso = True

while(paso):

    print("Bienvenido!")
    fecha = input("Para buscar su archivo de audio ingrese la fecha: ")

    for doc in coleccion2.find():
        if(doc['fecha_archivo'] == fecha):
            nom = doc["nombre_archivo"]

    nom = "salida" + nom
    data = coleccion2.find_one({'fecha_archivo': fecha})
        
    with open(nom, "wb") as f:
        f.write(data['file'])

    print("Reproduciendo audio...")
    
    playsound.playsound(nom)

    print("Completado :)")

    resp = input("Desea escuchar otro audio? (S/N): ")

    if(resp == "N"):
        paso = False


