# 1. Crear el diccionario
agenda = {
    "A123": {
        "Nombre":"Santiago Andrés",
        "Teléfono": 30451358,
        "Dirección": "Calle 75 #26-45"
    },
    "A456": {
        "Nombre":"Jesús Alberto",
        "Teléfono": 30451510,
        "Dirección": "Calle 76 #27-46"
    }
}
print(type(agenda), agenda)

# 2. Iterar sus elementos (son otros diccionarios)
for i in agenda:
    print(i,type(i))
    for j in agenda[i]:
        print(f"Su '{j}' es {agenda[i][j]}")