import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurante App - Sistema Base")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        # Inicializar los servicios centralizados
        self.restaurante_servicio = RestauranteServicio()

        # Contenedor principal de vistas
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.vista_actual = None
        self.cambiar_vista("LoginView")

    def cambiar_vista(self, nombre_vista):
        # Destruir la vista actual si existe
        if self.vista_actual is not None:
            self.vista_actual.destroy()

        # Instanciar y mostrar la nueva vista dentro de la misma ventana
        if nombre_vista == "LoginView":
            self.vista_actual = LoginView(self.container, self.cambiar_vista, self.restaurante_servicio)
        elif nombre_vista == "MainView":
            self.vista_actual = MainView(self.container, self.cambiar_vista, self.restaurante_servicio)

        self.vista_actual.pack(fill="both", expand=True)

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.ejecutar()