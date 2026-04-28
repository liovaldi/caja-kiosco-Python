#TP integrador – Repetitivas- Condicionales y Secuenciales. // Iovaldi Ludmila // Comision 2

#Ejercicio 1— “Caja del Kiosco” 
t_s_descuento= 0
t_c_descuento= 0

#Nombre
nombre = input("Por favor, escriba el nombre del cliente: ").strip()
while not nombre.isalpha() or nombre == "":
    print ("Error : ingrese un nombre que solo contenga letras.")
    nombre = input("Por favor, escriba el nombre del cliente: ").strip()

#Cantidad
cantidad_str = input("Ingrese la cantidad de productos a comprar : ").strip()
while not cantidad_str.isdigit() or int(cantidad_str)== 0:
    print("Error: ingrese un numero entero positivo mayor a 0" )
    cantidad_str = input("Ingrese la cantidad de productos a comprar : ").strip()
cantidad_int= int(cantidad_str)

#Precio
for cont in range (1, cantidad_int +1):
    precio_str = input(f"Ingrese el precio {cont} :").strip()
    while not precio_str.isdigit() or int(precio_str)== 0:
        print("Error: ingrese un numero entero: ")
        precio_str = input(f"Ingrese el precio {cont} :").strip()
    precio_int = int(precio_str)
    
#Descuento
    descuento = input("¿Tiene descuento? (S/N): ").lower().strip()
    while descuento != "s" and descuento != "n":
        print("Error: su respuesta debe ser S/N")
        descuento = input("¿Tiene descuento? (S/N): ").lower().strip()
    if descuento == ("s"):
        precio_descuento = precio_int*0.9
    else:
        precio_descuento = precio_int

    t_s_descuento=+ precio_int
    t_c_descuento=+ precio_descuento

ahorro= t_s_descuento-t_c_descuento
promedio = float(t_c_descuento/cantidad_int)

print(f"Total sin descuento: $ {t_s_descuento:.2f}")
print(f"Total con descuento: $ {t_c_descuento:.2f}")
print(f"Se ahorró: $ {ahorro:.2f}")
print(f"El promedio por producto es de: $ {promedio:.2f}")
