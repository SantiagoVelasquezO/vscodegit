import customtkinter as ctk

# Configuración inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Función para calcular el IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertir cm a metros
        imc = peso / (altura ** 2)
        imc = round(imc, 2)

        if imc < 18.5:
            estado = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            estado = "Normal"
        elif 25 <= imc < 29.9:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        resultado_label.configure(text=f"IMC: {imc} - {estado}")

    except ValueError:
        resultado_label.configure(text="Por favor ingresa valores válidos")

# Ventana principal
app = ctk.CTk()
app.title("Calculadora de IMC")
app.geometry("350x300")

# Widgets
titulo = ctk.CTkLabel(app, text="Calculadora de IMC", font=ctk.CTkFont(size=18, weight="bold"))
titulo.pack(pady=15)

entry_peso = ctk.CTkEntry(app, placeholder_text="Peso en kg (ej: 70)")
entry_peso.pack(pady=10)

entry_altura = ctk.CTkEntry(app, placeholder_text="Altura en cm (ej: 175)")
entry_altura.pack(pady=10)

btn_calcular = ctk.CTkButton(app, text="Calcular IMC", command=calcular_imc)
btn_calcular.pack(pady=15)

resultado_label = ctk.CTkLabel(app, text="")
resultado_label.pack(pady=10)

# Ejecutar app
app.mainloop()
