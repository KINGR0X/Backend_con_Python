# ===Concatenar valores===

name = "Elian"
last_name = "Reyes"

# Concatenar Strins y guardarlos en una varibale
full_name = name+" "+last_name
print(full_name)

# Comillas simples para evitar problemas
print('She said "Hello"')

# === 2da forma de concatenar ===

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print("v2", template)

# === 3ra forma de concatenar ===

# Para esta forma es necesario colcocar una "f" al inicio del texto a concatenar

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"

print("v3", template)
