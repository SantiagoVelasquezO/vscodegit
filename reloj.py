import customtkinter as ctk
import time

# Configuración inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Función para actualizar la hora
def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")
    reloj_label.configure(text=hora_actual)
    app.after(1000, actualizar_hora)  # actualiza cada segundo

# Ventana principal
app = ctk.CTk()
app.title("Reloj Digital")
app.title("Reloj Digital")
app.title("Reloj Digital")
app.geometry("300x200")

# Título
titulo = ctk.CTkLabel(app, text="Reloj Digital", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=20)

# Etiqueta de hora
reloj_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=40))
reloj_label.pack()

# Iniciar reloj
actualizar_hora()
# actualizar_hora()
# actualizar_hora()
# actualizar_hora()
# actualizar_hora()

# Ejecutar app
app.mainloop()
