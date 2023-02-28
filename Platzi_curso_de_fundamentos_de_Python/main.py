# Juego piedra, papel, o tigera

user_option = input("piedra, papel o tijera =>").lower().strip()

computer_option = "piedra"

print("\n======")
print("User:", user_option)
print("pc:", computer_option)
print("")

if user_option == computer_option:
    print("=== Empate ===")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("=== Ganaste ===")
    else:
        print("===Perdiste===")
elif user_option == "papel":
    if computer_option == "piedra":
        print("=== Ganaste ===")
    else:
        print("===Perdiste===")
elif user_option == "tijera":
    if computer_option == "papel":
        print("=== Ganaste ===")
    else:
        print("===Perdiste===")
else:
    print("===No se ingreso una opción valida===")
