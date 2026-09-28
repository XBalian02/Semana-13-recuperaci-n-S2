import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, controlador, restaurante_servicio):
        super().__init__(parent, bg="#f0f0f0")
        self.controlador = controlador
        self.restaurante_servicio = restaurante_servicio

        self.crear_widgets()

    def crear_widgets(self):
        # Título
        titulo = tk.Label(self, text="Restaurante App - Acceso", font=("Arial", 18, "bold"), bg="#f0f0f0")
        titulo.pack(pady=20)

        # Marco del formulario
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(pady=10)

        lbl_usuario = tk.Label(form_frame, text="Usuario:", font=("Arial", 12), bg="#f0f0f0")
        lbl_usuario.grid(row=0, column=0, sticky="w", pady=5)
        self.txt_usuario = tk.Entry(form_frame, font=("Arial", 12))
        self.txt_usuario.grid(row=0, column=1, pady=5)

        lbl_password = tk.Label(form_frame, text="Contraseña:", font=("Arial", 12), bg="#f0f0f0")
        lbl_password.grid(row=1, column=0, sticky="w", pady=5)
        self.txt_password = tk.Entry(form_frame, show="*", font=("Arial", 12))
        self.txt_password.grid(row=1, column=1, pady=5)

        # Botón de ingreso
        btn_ingresar = tk.Button(self, text="Ingresar", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.verificar_login)
        btn_ingresar.pack(pady=20)

    def verificar_login(self):
        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        if self.restaurante_servicio.validar_credenciales(usuario, password):
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}")
            self.controlador("MainView")
        else:
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos.")