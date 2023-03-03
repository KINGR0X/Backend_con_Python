person = {
    "name": "nico",
    "last_name": "molina",
    "langs": ["python", "javascript"],
    "age": 29
}

# === cambio de valores ===
person["name"] = "santi"
person["langs"].append("rust")

# === Eliminar valor ===
del person["last_name"]
person.pop("age")


print(person)

# === devuleve los items separados como tuplas ===
print(person.items())

# === Devuelve solo las keys ===
print(person.keys())

# === Devuelve una lista de solo los valores===
print(person.values())
