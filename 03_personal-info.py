nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
if int(edad)>=0 and int(edad)<=15:
    print("Es un niño")
elif int(edad)>=16 and int(edad)<=40:
    print("Es joven")
elif int(int(edad))>=41 and int(edad)<=150:
    print("Es adulto")
else:
    print("No es un dato válido")

ubicacion= input("Ingrese su ubicación: ")
print("Bienvenido a casa amo y señor ", nombre, apellido, 
      "de",ubicacion, "poderoso de nivel",edad)
