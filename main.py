import random
import string
from colorama import init, Fore

init(autoreset=True)

def generar_mensaje():
    mensaje = "[+] " + "https://discord.gift/" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return mensaje

print(Fore.BLUE + "╔═╗─╔╗╔╗──────╔═══╗─────────────╔╗")
print(Fore.BLUE + "║║╚╗║╠╝╚╗─────║╔═╗║────────────╔╝╚╗") 
print(Fore.BLUE + "║╔╗╚╝╠╗╔╬═╦══╗║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬══╦═╗")
print(Fore.BLUE + "║║╚╗║╠╣║║╔╣╔╗║║║╔═╣║═╣╔╗╣║═╣╔╣╔╗║║║╔╗║╔╝")
print(Fore.BLUE + "║║─║║║║╚╣║║╚╝║║╚╩═║║═╣║║║║═╣║║╔╗║╚╣╚╝║║")
print(Fore.BLUE + "╚╝─╚═╩╩═╩╝╚══╝╚═══╩══╩╝╚╩══╩╝╚╝╚╩═╩══╩╝")
print(Fore.BLUE + "Created by l3vik")

def main():
    try:
        cantidad_mensajes = int(input( "[?] " + "How much nitro codes want to generate?: "))
        for _ in range(cantidad_mensajes):
            mensaje = generar_mensaje()
            print(Fore.GREEN + mensaje)
    except ValueError:
        print("Plese, select a valid number")

if __name__ == "__main__":
    main()

