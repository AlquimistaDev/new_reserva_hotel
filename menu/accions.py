import sqlite3

# Importar la consulta desde el archivo SQL
with open('./queries/get_hab_disp.sql', 'r') as file:
    CONSULTA_OBTENER_HABITACION = file.read()


def accion1(texto, conexion):
    texto.configure(text='Has elegido la opción 1 del menú principal')
    # Ejemplo de consulta
    cursor = conexion.cursor()
    cursor.execute(CONSULTA_OBTENER_HABITACION)
    resultado = cursor.fetchone()
    texto.configure(text=f'Resultado de la consulta: {resultado}')
    cursor.close()

def accion2(texto, conexion):
    texto.configure(text='Has elegido la opción 2 del menú principal')
    # Puedes realizar otra consulta aquí

def acciona(texto, conexion):
    texto.configure(text='Has elegido la opción a del submenú')
    # Puedes realizar otra consulta aquí

def accionb(texto, conexion):
    texto.configure(text='Has elegido la opción b del submenú')
    # Puedes realizar otra consulta aquí