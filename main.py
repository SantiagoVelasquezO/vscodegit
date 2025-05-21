import customtkinter as ctk
import string
import random

# Configuración inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Función para generar la contraseña
def generar_contrasena():
    longitud = int(entry_longitud.get())
    incluir_mayusculas = var_mayus.get()
    incluir_minusculas = var_minus.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()

    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        resultado_label.configure(text="¡Selecciona al menos un tipo de carácter!")
        return

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    resultado_label.configure(text=f"Contraseña generada:\n{contrasena}")

# Ventana principal
app = ctk.CTk()
app.title("Generador de Contraseñas")
app.geometry("400x400")

# Widgets
titulo = ctk.CTkLabel(app, text="Generador de Contraseñas Seguras", font=ctk.CTkFont(size=18, weight="bold"))
titulo.pack(pady=10)

entry_longitud = ctk.CTkEntry(app, placeholder_text="Longitud (ej: 12)")
entry_longitud.pack(pady=10)

var_mayus = ctk.BooleanVar(value=True)
check_mayus = ctk.CTkCheckBox(app, text="Incluir mayúsculas", variable=var_mayus)
check_mayus.pack()

var_minus = ctk.BooleanVar(value=True)
check_minus = ctk.CTkCheckBox(app, text="Incluir minúsculas", variable=var_minus)
check_minus.pack()

var_numeros = ctk.BooleanVar(value=True)
check_numeros = ctk.CTkCheckBox(app, text="Incluir números", variable=var_numeros)
check_numeros.pack()

var_simbolos = ctk.BooleanVar(value=False)
check_simbolos = ctk.CTkCheckBox(app, text="Incluir símbolos", variable=var_simbolos)
check_simbolos.pack()

btn_generar = ctk.CTkButton(app, text="Generar Contraseña", command=generar_contrasena)
btn_generar.pack(pady=15)

resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=10)

# Ejecutar app
app.mainloop()
# Ejecutar app
# Ejecutar app
# Ejecutar app
# Ejecutar app
