from login.login import iniciar_login, login_exitoso
from  menu.interface import crear_menu

def main():
    iniciar_login()

    if login_exitoso:
        print("El login fue exitoso")

        crear_menu()

if __name__ == "__main__":
    main()