from pymongo import MongoClient

mongo = MongoClient('localhost')

baseDatos = mongo['FuentesSonorasAmbientales']

coleccion1 = baseDatos['archivos']

coleccion1.insert_many([{    
    'idArch' : "0",
    'fecha_de_grabacion' : "25/12/1999",
    'ciudad' : "Valdivia",
    'duracion' : "00:25",
    'formato' : "wav",
    'latitud' : -39.831271357397846,
    'longitud' : -73.24012245113406,
    'ubicacion' : "interior",
    'usuario' : {
		'rut' : "11111111-1",
		'nombre' : "Nicolas",
		'apellido' : "Saldivia"
    },
    'segmentos' : [{
                    'idSeg' : "0",
                    'formato' : "wav",  
                    'duracion' : "00:20",
                    'inicio' :  "00:05",
                    'fin' : "00:25",
                    'etiquetas' : [{
                                    'nombre_fuente' : "bebe",
                                    'descripcion' : "llanto de un bebe recien nacido",
                                    'id_analizador' : "0"
                    }]
    }]                             
    },
{
    'idArch' : "1",
    'fecha_de_grabacion' : "21/09/2020",
    'ciudad' : "Valdivia",
    'duracion' : "00:51",
    'formato' : "wav",
    'latitud' : -39.80704986934237,
    'longitud' : -73.21996949173386,
    'ubicacion' : "exterior",
    'usuario' : {
		'rut' : "22222222-2",
		'nombre' : "Jesús",
		'apellido' : "Madariaga"
    },
    'segmentos' : [{
                    'idSeg' : "0",
                    'formato' : "wav",  
                    'duracion' : "00:13",
                    'inicio' :  "00:07",
                    'fin' : "00:20",
                    'etiquetas' : [{
                                    'nombre_fuente' : "disparos",
                                    'descripcion' : "balazera en plena calle",
                                    'id_analizador' : "1"
                    }]
    }]                             
    },
{
    'idArch' : "2",
    'fecha_de_grabacion' : "13/01/2021",
    'ciudad' : "Valdivia",
    'duracion' : "00:27",
    'formato' : "wav",
    'latitud' : -39.807076,
    'longitud' : -73.264808,
    'ubicacion' : "exterior",
    'usuario' : {
		'rut' : "33333333-3",
		'nombre' : "Jessica",
		'apellido' : "Delgado"
    },
    'segmentos' : [{
                    'idSeg' : "0",
                    'formato' : "wav",  
                    'duracion' : "00:05",
                    'inicio' :  "00:00",
                    'fin' : "00:05",
                    'etiquetas' : [{
                                    'nombre_fuente' : "Perro",
                                    'descripcion' : "Ladridos de perro en una poblacion",
                                    'id_analizador' : "2"
                    }]
    }]                             
    }])


print("Datos ingresados!!!")
    
