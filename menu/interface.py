import tkinter as tk
from .accions import accion1, accion2, acciona, accionb

def crear_menu(conexion):
    ventana = tk.Tk()
    ventana.title('Ventana principal')
    ventana.geometry('800x600')

    barra_menus = tk.Menu(ventana)
    ventana.config(menu=barra_menus)

    menu = tk.Menu(barra_menus, tearoff=False)

    texto = tk.Label(ventana, text='¡Hola, desde Código Pitón!')
    texto.place(x=200, y=200)

    menu.add_command(label='Reservar', command=lambda: accion1(texto, conexion))
    menu.add_command(label='Opción 2', command=lambda: accion2(texto, conexion))

    submenu = tk.Menu(menu, tearoff=False)
    submenu.add_command(label='Opción A', command=lambda: acciona(texto, conexion))
    submenu.add_command(label='Opción B', command=lambda: accionb(texto, conexion))

    menu.add_cascade(label='Submenú', menu=submenu)

    menu.add_separator()
    menu.add_command(label='Salir', command=lambda: cerrar_aplicacion(ventana, conexion))

    barra_menus.add_cascade(label="Menú", menu=menu)

    ventana.mainloop()

def cerrar_aplicacion(ventana, conexion):
    if conexion:
        conexion.close()
    ventana.destroy()