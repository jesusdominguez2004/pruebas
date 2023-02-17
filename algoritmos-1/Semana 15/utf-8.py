with open("utf-8.txt", "w", encoding="utf-8") as file:
    x = "aeiouñ"
    y = "áéíóúñ"
    
    file.write(x + " " + x.upper() + "\n")
    file.write(y + " " + y.upper())

with open("utf-8.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print(contenido)
