from database.config import connection
from menu.interface import crear_menu

def main():
    conn = connection()
    if conn:
        print("La conexión fue exitosa")
    else:
        print("Error en la conexión")
    
    crear_menu()

if __name__ == '__main__':
    main()
