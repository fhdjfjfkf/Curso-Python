import random
caracteres = "+~/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""


while True:
    try:
        passlen = int(input("Ingrese la longitud de la clave: "))
        break
    except ValueError:
        print("Ingrese un número entero válido.")


for i in range(passlen):
    selectecaracter = random.choice(caracteres)
    password += selectecaracter

print(password)
