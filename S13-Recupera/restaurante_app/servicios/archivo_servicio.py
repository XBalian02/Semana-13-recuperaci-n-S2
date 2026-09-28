import json
import os

class ArchivoServicio:
    def cargar_json(self, nombre_archivo):
        ruta = os.path.join(os.path.dirname(__file__), '..', 'datos', nombre_archivo)
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r', encoding='utf-8') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []

    def guardar_json(self, nombre_archivo, datos):
        ruta = os.path.join(os.path.dirname(__file__), '..', 'datos', nombre_archivo)
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)