import tkinter as tk
from .accions import accion1, accion2, acciona, accionb

def crear_menu():
    # Creamos la ventana principal.
    ventana = tk.Tk()
    ventana.title('Ventana principal')  # Establece el título de la ventana.
    ventana.geometry('800x600')  # Establece el tamaño de la ventana.

    # Creamos una barra de menús y la añadimos a la ventana principal.
    barra_menus = tk.Menu(ventana)
    ventana.config(menu=barra_menus)  # Configuramos la ventana para que use la barra de menús.

    # Creamos un menú cuyo contenedor será la barra de menús.
    menu = tk.Menu(barra_menus, tearoff=False)

    # Añadimos opciones al menú indicando su nombre y acción asociada.
    texto = tk.Label(ventana, text='¡Hola, desde Código Pitón!')  # Creamos una etiqueta con un mensaje inicial.
    texto.place(x=200, y=200)  # Posicionamos la etiqueta en la ventana.

    menu.add_command(label='Reservar', command=lambda: accion1(texto))  # Añade una opción al menú que ejecuta `accion1`.
    menu.add_command(label='Opción 2', command=lambda: accion2(texto))  # Añade una opción al menú que ejecuta `accion2`.

    # Creamos un submenú.
    submenu = tk.Menu(menu, tearoff=False)
    submenu.add_command(label='Opción A', command=lambda: acciona(texto))  # Añade una opción al submenú que ejecuta `acciona`.
    submenu.add_command(label='Opción B', command=lambda: accionb(texto))  # Añade una opción al submenú que ejecuta `accionb`.

    # Añadimos el submenú al menú principal.
    menu.add_cascade(label='Submenú', menu=submenu)  # Añade el submenú al menú principal bajo el nombre 'Submenú'.

    # Añadimos una línea separadora y la opción de salir.
    menu.add_separator()  # Añade una línea separadora al menú.
    menu.add_command(label='Salir', command=ventana.destroy)  # Añade una opción al menú que cierra la ventana.

    # Finalmente, añadimos el menú a la barra de menús.
    barra_menus.add_cascade(label="Menú", menu=menu)  # Añade el menú a la barra de menús bajo el nombre 'Menú'.

    ventana.mainloop()  # Ejecutamos la ventana principal para que se mantenga abierta y responda a eventos.
