import tkinter as tk
from tkinter import messagebox
from database.config import connection  # Importamos la función connection desde database.config
from menu.interface import crear_menu

# Variable global para indicar si el login fue exitoso
login_exitoso = False

def conn(usuario, password):
    # Realizar la conexión con la base de datos utilizando la función connection
    return connection(usuario, password)

def verificar_login():
    global login_exitoso
    usuario = entry_usuario.get()
    password = entry_password.get()
    
    # Aquí puedes realizar validaciones adicionales si es necesario

    # Verificar la conexión y el login
    if conn(usuario, password):
        login_exitoso = True
        messagebox.showinfo("Login exitoso", f"Bienvenido, {usuario}!")
        root.withdraw()  # Ocultar la ventana de login
        crear_menu()  # Llamar a la función para crear el menú principal después del login
    else:
        mostrar_error_login()

def mostrar_error_login():
    error_window = tk.Toplevel(root)
    error_window.title("Error de Login")
    
    label_error = tk.Label(error_window, text="Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
    label_error.pack(pady=10)
    
    button_retry = tk.Button(error_window, text="Volver a intentar", command=lambda: [error_window.destroy(), mostrar_ventana_login()])
    button_retry.pack(pady=5)

def mostrar_ventana_login():
    entry_usuario.delete(0, tk.END)  # Borrar el contenido del campo de usuario
    entry_password.delete(0, tk.END)  # Borrar el contenido del campo de contraseña
    root.deiconify()  # Mostrar la ventana de login nuevamente

def iniciar_login():
    global root, entry_usuario, entry_password

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ventana de Login")

    # Crear los widgets (etiquetas, entradas y botones)
    label_usuario = tk.Label(root, text="Usuario:")
    label_usuario.pack(pady=10)
    entry_usuario = tk.Entry(root)
    entry_usuario.pack(pady=5)

    label_password = tk.Label(root, text="Contraseña:")
    label_password.pack(pady=10)
    entry_password = tk.Entry(root, show="*")  # show="*" para ocultar la contraseña
    entry_password.pack(pady=5)

    button_login = tk.Button(root, text="Login", command=verificar_login)
    button_login.pack(pady=20)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()

if __name__ == "__main__":
    iniciar_login()
