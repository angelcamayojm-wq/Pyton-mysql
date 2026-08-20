       # Menú para escoger categoría
print("\nCategorías disponibles:")
print("1. Electrodoméstico")
print("2. Tecnología")
print("3. Ropa")
print("4. Calzado")
print("5. Deportes")
        
opcion = input("Seleccione el número de la categoría (1-5): ")
        
        # Asignar la categoría según el número que escogió
if opcion == "1":
            categoria = "Electrodoméstico"
elif opcion == "2":
            categoria = "Tecnología"
elif opcion == "3":
            categoria = "Ropa"
elif opcion == "4":
            categoria = "Calzado"
elif opcion == "5":
            categoria = "Deportes"
else:
            categoria = "Sin categoría" # Por si se equivoca
