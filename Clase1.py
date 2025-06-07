palabras = {
    "lol": "Abreviasion de la expresion 'laugh out loud' que significa 'reír a carcajadas'",
    "cringe": "Significa verguenza ajena",
    "rofl": "Una respuesta a una broma",
    "sheesh": "Ligera desaprovacion",
    "creepy": "Algo aterrador",
    "parry": "Bloqueo perfecto en un videojuego",
    "tryhard": "Se refiere a una persona que le pone mucho esfuerzo a algo",
    "iframe": "Se refiere a los momentos de ivencivilidad en un videojuego",
    "ping": "Se refiere a la velocidad de una conexión a internet",
}
print ("Palabras:")
for palabra in palabras:
    print(f"{palabra}")

pregunta = input("Ingrese la palabra de la que quiera saber el significado: ").lower()

if pregunta in palabras:
    print(palabras[pregunta])
else:
    print("No existe")
