# from login.login import iniciar_login, login_exitoso
# from menu.interface import crear_menu

# def main():
#     iniciar_login()

#     if login_exitoso:
#         print("El login fue exitoso")
#         crear_menu()
#     else:
#         print("El login no fue exitoso")

# if __name__ == "__main__":
#     main()

from login.login import iniciar_login, login_exitoso, conexion_db

def main():
    iniciar_login()

    if login_exitoso:
        print("El login fue exitoso")
        # No necesitamos llamar a crear_menu() aquí, ya se llama en verificar_login()
    else:
        print("El login no fue exitoso")

if __name__ == "__main__":
    main()