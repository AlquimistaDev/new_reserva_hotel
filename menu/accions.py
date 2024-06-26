import sqlite3
import tkinter as tk
from tkinter import ttk

# Importar la consulta desde el archivo SQL
with open('./queries/get_hab_disp.sql', 'r') as file:
    CONSULTA_OBTENER_HABITACION = file.read()


def accion1(texto, conexion):
    texto.configure(text='Has elegido la opción 1 del menú principal')
    # Ejemplo de consulta
    cursor = conexion.cursor()
    cursor.execute(CONSULTA_OBTENER_HABITACION)
    resultado = cursor.fetchall()
    # Llenar la tabla con datos
    llenar_tabla(resultado)
    cursor.close()

#Funcion llenar tabla -> optimizacion sacar de este scope
def llenar_tabla(resultado):
    crear_tabla()
    print(resultado)
    # for habitacion in resultado:
    #     tabla.insert('', 'end', 
    #         values=(
    #             habitacion.numero_habitacion,
    #             habitacion.capacidad,
    #             habitacion.descripcion,
    #             habitacion.tipo_cama,
    #             habitacion.estado_hab))
    for habitacion in resultado:
        tabla.insert('', 'end', values=habitacion)


# Crear la ventana principal de Tkinter
def crear_tabla():
    global tabla
    root = tk.Tk()
    root.title("Tabla de Personas")
    # Crear el widget Treeview (tabla)
    tabla = ttk.Treeview(root, columns=('Numero de Habitacion',
                                        'Capacidad',
                                        'Descripcion',
                                        'Tipo Cama',
                                        'Estado Habitacion',), show='headings')
    # Definir encabezados de columna
    tabla.heading('Numero de Habitacion', text='Numero de Habitacion')
    tabla.heading('Capacidad', text='Capacidad')
    tabla.heading('Descripcion', text='Descripcion')
    tabla.heading('Tipo Cama', text='Tipo Cama')
    tabla.heading('Estado Habitacion', text='Estado Habitacion')

    # Ajustar las columnas
    for col in ('Numero de Habitacion','Capacidad','Descripcion','Tipo Cama','Estado Habitacion',):
        tabla.column(col, anchor=tk.CENTER)

    # Empaquetar la tabla en la ventana
    tabla.pack(padx=15, pady=50)

def accion2(texto, conexion):
    texto.configure(text='Has elegido la opción 2 del menú principal')
    # Puedes realizar otra consulta aquí

def acciona(texto, conexion):
    texto.configure(text='Has elegido la opción a del submenú')
    # Puedes realizar otra consulta aquí

def accionb(texto, conexion):
    texto.configure(text='Has elegido la opción b del submenú')
    # Puedes realizar otra consulta aquí