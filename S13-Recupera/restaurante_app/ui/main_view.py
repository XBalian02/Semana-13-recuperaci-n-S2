import tkinter as tk
from tkinter import messagebox

class MainView(tk.Frame):
    def __init__(self, parent, controlador, restaurante_servicio):
        super().__init__(parent, bg="#ffffff")
        self.controlador = controlador
        self.restaurante_servicio = restaurante_servicio

        self.crear_widgets()

    def crear_widgets(self):
        # Barra superior / Encabezado
        header = tk.Frame(self, bg="#333333", height=50)
        header.pack(fill="x", side="top")

        lbl_titulo = tk.Label(header, text="Panel Principal - Restaurante App", font=("Arial", 14, "bold"), fg="white", bg="#333333")
        lbl_titulo.pack(side="left", padx=15, pady=10)

        btn_salir = tk.Button(header, text="Cerrar Sesión", bg="#f44336", fg="white", command=lambda: self.controlador("LoginView"))
        btn_salir.pack(side="right", padx=15, pady=10)

        # Contenedor de opciones / contenido central
        content_frame = tk.Frame(self, bg="#ffffff")
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Botones de consulta
        btn_productos = tk.Button(content_frame, text="Ver Productos", font=("Arial", 11), width=20, bg="#2196F3", fg="white", command=self.mostrar_productos)
        btn_productos.grid(row=0, column=0, padx=10, pady=10)

        btn_usuarios = tk.Button(content_frame, text="Ver Usuarios", font=("Arial", 11), width=20, bg="#FF9800", fg="white", command=self.mostrar_usuarios)
        btn_usuarios.grid(row=0, column=1, padx=10, pady=10)

        # Funcionalidad Futura (Pendiente)
        btn_ventas = tk.Button(content_frame, text="Ventas (Pendiente)", font=("Arial", 11), width=20, bg="#9e9e9e", fg="white", state="disabled")
        btn_ventas.grid(row=0, column=2, padx=10, pady=10)

        # Área de visualización (Listbox con Scrollbar)
        list_frame = tk.Frame(self)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_info = tk.Label(list_frame, text="Seleccione una opción arriba para consultar información.", font=("Arial", 11, "italic"))
        self.lbl_info.pack(anchor="w", pady=5)

        self.listbox = tk.Listbox(list_frame, font=("Courier", 11), width=80, height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

    def mostrar_productos(self):
        self.listbox.delete(0, tk.END)
        productos = self.restaurante_servicio.obtener_productos()
        self.lbl_info.config(text="Listado de Productos Registrados:")
        for p in productos:
            self.listbox.insert(tk.END, f"ID: {p.id:<3} | Nombre: {p.nombre:<25} | Precio: ${p.precio:<6.2f} | Stock: {p.stock}")

    def mostrar_usuarios(self):
        self.listbox.delete(0, tk.END)
        usuarios = self.restaurante_servicio.obtener_usuarios()
        self.lbl_info.config(text="Listado de Usuarios Registrados:")
        for u in usuarios:
            self.listbox.insert(tk.END, f"Usuario: {u.username:<15} | Rol: {u.rol}")