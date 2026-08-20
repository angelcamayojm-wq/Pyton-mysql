import pymysql as mysql

user = "root"
password = "root"       
host = "localhost"      
baseDatos = "tienda_adso" 

try:
    # Se crea la conexión y el cursor DENTRO del try
    miConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
    cursor = miConexion.cursor()
    print("¡Conexión exitosa a la base de datos!\n")

    # --- A PARTIR DE AQUÍ, TODAS LAS FUNCIONES ESTÁN DENTRO DEL TRY ---

    def agregar():
        try:
            print("\n--- NUEVO PRODUCTO ---")
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))

            print("\nSeleccione una categoría:")
            print("1. Electrodoméstico")
            print("2. Tecnología")
            print("3. Ropa")
            print("4. Calzado")
            print("5. Deportes")
            
            opcion = input("Ingrese el número de la categoría (1-5): ")
            
            if opcion in ["1", "2", "3", "4", "5"]:
                idCategoria = int(opcion)
            else:
                print("Opción inválida. Se asignará 'Electrodoméstico' por defecto.")
                idCategoria = 1

            producto = (codigo, nombre, precio, idCategoria) 
            consulta = "insert into productos (proCodigo, proNombre, proPrecio, idCategoria) values (%s, %s, %s, %s)"
            
            cursor.execute(consulta, producto)
            miConexion.commit()
            
            if(cursor.rowcount == 1):
                print("¡Producto agregado correctamente!")
                
        except ValueError:
            print("Error: El precio debe ser un número válido (usando punto).")
        except miConexion.Error as e:
            miConexion.rollback()
            print("Error al agregar producto:", str(e))

    def listar():
        try:
            consulta = """
                SELECT p.idProducto, p.proCodigo, p.proNombre, p.proPrecio, c.nombreCategoria 
                FROM productos p
                JOIN categorias c ON p.idCategoria = c.idCategoria
            """
            cursor.execute(consulta)
            productos = cursor.fetchall()
            
            if not productos:
                print("\n--- No hay productos registrados aún ---")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for p in productos:
                    print(f"ID: {p[0]} | Código: {p[1]} | Nombre: {p[2]} | Precio: {p[3]} | Categoría: {p[4]}")
                    
        except miConexion.Error as e:
            print("Error al listar productos:", str(e))

    def consultarPorCodigo(codigo):
        try:
            consulta = """
                SELECT p.idProducto, p.proCodigo, p.proNombre, p.proPrecio, c.nombreCategoria 
                FROM productos p
                JOIN categorias c ON p.idCategoria = c.idCategoria
                WHERE p.proCodigo = %s
            """
            cursor.execute(consulta, (codigo,))
            producto = cursor.fetchone()
            
            if producto:
                print("\n--- PRODUCTO ENCONTRADO ---")
                print(f"ID: {producto[0]}")
                print(f"Código: {producto[1]}")
                print(f"Nombre: {producto[2]}")
                print(f"Precio: {producto[3]}")
                print(f"Categoría: {producto[4]}")
            else:
                print(f"No existe ningún producto con el código '{codigo}'")
                
        except miConexion.Error as e:
            print("Error al consultar:", str(e))

    def agregar50():
        try:
            print("\nCargando 50 productos de prueba...")
            productos = [
                ("ELEC001", "Neviera Haceb 14 pies", 2500000, 1), ("ELEC002", "Lavadora Samsung 20kg", 1800000, 1),
                ("ELEC003", "Microondas Whirlpool", 450000, 1), ("ELEC004", "Licuadora Oster 800W", 220000, 1),
                ("ELEC005", "Plancha Black&Decker", 150000, 1), ("ELEC006", "Batidora KitchenAid", 800000, 1),
                ("ELEC007", "Cafetera Dolce Gusto", 350000, 1), ("ELEC008", "Horno Eléctrico Mabe", 1200000, 1),
                ("ELEC009", "Aspiradora Electrolux", 600000, 1), ("ELEC010", "TV LG 55 Pulgadas", 2100000, 1),
                ("TEC001", "Laptop Asus ROG", 3500000, 2), ("TEC002", "Celular Samsung S23", 4200000, 2),
                ("TEC003", "Tablet iPad Air", 2800000, 2), ("TEC004", "Audífonos Sony", 350000, 2),
                ("TEC005", "Monitor LG 24 Pulgadas", 900000, 2), ("TEC006", "Mouse Logitech Gamer", 120000, 2),
                ("TEC007", "Teclado Mecánico Redragon", 250000, 2), ("TEC008", "Parlante JBL Boombox", 550000, 2),
                ("TEC009", "Impresora HP Multifuncional", 700000, 2), ("TEC010", "Disco Duro Externo 1TB", 350000, 2),
                ("ROPA001", "Camisa Polo Ralph Lauren", 150000, 3), ("ROPA002", "Pantalón Levis Original", 280000, 3),
                ("ROPA003", "Chaquetón Adidas", 450000, 3), ("ROPA004", "Suéter de lana", 180000, 3),
                ("ROPA005", "Jean Slim Fit", 220000, 3), ("ROPA006", "Camiseta Deportiva Nike", 120000, 3),
                ("ROPA007", "Blusa Seda", 190000, 3), ("ROPA008", "Abrigo Invierno", 550000, 3),
                ("ROPA009", "Short y Conjunto", 150000, 3), ("ROPA010", "Pijama Invierno", 130000, 3),
                ("ZAPA001", "Zapatillas Nike Running", 350000, 4), ("ZAPA002", "Tenis Adidas Campus", 420000, 4),
                ("ZAPA003", "Botas de Cuero", 580000, 4), ("ZAPA004", "Sandalias Crocs", 150000, 4),
                ("ZAPA005", "Zapatos Formales", 300000, 4), ("ZAPA006", "Tacones", 250000, 4),
                ("ZAPA007", "Zapatillas Puma", 320000, 4), ("ZAPA008", "Mocasines", 280000, 4),
                ("ZAPA009", "Botas de Lluvia", 200000, 4), ("ZAPA010", "Chanclas", 50000, 4),
                ("DEP001", "Bicicleta Italiana Ruta", 2800000, 5), ("DEP002", "Pesa de Hierro 20kg", 250000, 5),
                ("DEP003", "Balón de Fútbol", 120000, 5), ("DEP004", "Patines en línea", 450000, 5),
                ("DEP005", "Colchoneta de Yoga", 80000, 5), ("DEP006", "Cuerda de Saltar", 50000, 5),
                ("DEP007", "Guantes de Boxeo", 180000, 5), ("DEP008", "Tabla de Surf", 650000, 5),
                ("DEP009", "Mochila de Montaña", 280000, 5), ("DEP010", "Tenis de Pádel", 380000, 5)
            ]
            
            consulta = "insert into productos (proCodigo, proNombre, proPrecio, idCategoria) values (%s, %s, %s, %s)"
            cursor.executemany(consulta, productos)
            miConexion.commit()
            
            if (cursor.rowcount == len(productos)):
                print(f"¡Éxito! Se agregaron {len(productos)} productos.")
            else:
                print("Algo salió mal.")
                
        except miConexion.Error as e:
            miConexion.rollback()
            print("Error al agregar los 50 productos:", str(e))

    def menu_principal():
        while True:
            print("\n" + "="*30)
            print("       MENÚ PRINCIPAL")
            print("="*30)
            print("1. Agregar un producto")
            print("2. Listar todos los productos")
            print("3. Consultar producto por código")
            print("4. Salir")
            print("="*30)
            
            opcion = input("Seleccione una opción (1-4): ")
            
            if opcion == "1":
                agregar()
            elif opcion == "2":
                listar()
            elif opcion == "3":
                codigo_buscar = input("Ingrese el código del producto a buscar: ")
                consultarPorCodigo(codigo_buscar)
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida, por favor intente de nuevo.")

    # --- ZONA DE INICIO ---
    # (Descomenta la siguiente línea solo la PRIMERA vez que ejecutes el código para tener datos)
    agregar50() 
    
    menu_principal()

    # Cerrar conexión al salir del menú
    cursor.close()
    miConexion.close()
    print("\nConexión cerrada.")

except Exception as e:
    print("Error general de conexión:", str(e))