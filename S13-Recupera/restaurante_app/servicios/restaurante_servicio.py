import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        self.productos = []
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        # Cargar usuarios
        datos_usuarios = self.archivo_servicio.cargar_json("usuarios.json")
        self.usuarios = [
            Usuario(u["username"], u["password"], u["rol"]) 
            for u in datos_usuarios
        ]

        # Cargar productos
        datos_productos = self.archivo_servicio.cargar_json("productos.json")
        self.productos = [
            Producto(p["id"], p["nombre"], p["precio"], p["categoria"]) 
            for p in datos_productos
        ]

    def guardar_datos(self):
        # Guardar usuarios
        datos_usuarios = [
            {"username": u.username, "password": u.password, "rol": u.rol} 
            for u in self.usuarios
        ]
        self.archivo_servicio.guardar_json("usuarios.json", datos_usuarios)

        # Guardar productos
        datos_productos = [
            {"id": p.id, "nombre": p.nombre, "precio": p.precio, "categoria": p.categoria} 
            for p in self.productos
        ]
        self.archivo_servicio.guardar_json("productos.json", datos_productos)

    def validar_usuario(self, username, password):
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                return usuario
        return None

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_datos()

    def obtener_productos(self):
        return self.productos
    
    def validar_credenciales(self, username, password):
        return self.validar_usuario(username, password)