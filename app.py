import pymysql as mysql


user = "root"
password = "root"       
host = "localhost"      
baseDatos = "tienda_adso" 


try:

    miConexion = mysql.connect(host=host, user=user, password=password, database=baseDatos)
    
    cursor = miConexion.cursor()
    print("¡Conexión exitosa a la base de datos!")

  
    def agregar():
        try:
            
            producto = (15, "TV", 25000.00, "Electrodoméstico")
            
           
            consulta = "insert into productos (proCodigo, proNombre, proPrecio, proCategoria) values (%s, %s, %s, %s)"
            
            cursor.execute(consulta, producto)
            miConexion.commit()
            
            if(cursor.rowcount == 1):
                print("Producto agregado correctamente")
                
        except miConexion.Error as e:
            miConexion.rollback()
            print("Error al agregar producto:", str(e))


    agregar()

    
    cursor.close()
    miConexion.close()

except Exception as e:
    print("Error general de conexión:", str(e))

def listar():
    try:
        consulta = "select * from productos"
        cursor.execute(consulta)
        productos = cursor.fetchall()
        for p in productos:
            print(p)
            print(p[0],p[1],p[2],p[3])
    except miConexion.Error as e:
        print(str(e))

def consultarPorCodigo(codigo):
    """
    Función que permite consultar un producto
    por su código
    """
    try:
        # Aquí se usa el 'codigo' que recibió la función
        consulta = "select * from productos where proCodigo=%s"
        cursor.execute(consulta, (codigo,)) # Nota: se pone (codigo,) para que sea una tupla
        producto = cursor.fetchone()
        if producto:
            print("Producto encontrado: ", producto)
            print("Producto encontrado:", producto[0], producto[1], 
                  producto[2], producto[3], producto[4])
        else:
            print("No existe producto con ese código")
    except miConexion.Error as e:
        print(str(e))

def actualizar():
    try:
        #producto a actualizar identificado con código 16
        datoActualizar=("Nevekon",450000, 16)
        consulta="update productos set proNombre=%s, proPrecio=%s where proCodigo=%s"
        resultado=cursor.execute(consulta,datoActualizar)
        miConexion.commit()
        if (cursor.rowcount==1):
            print("Producto actualizado correctamente")
        else:
            print("No existe producto con ese código")
    except miConexion.Error as e:
        miConexion.rollback()
        print(str(e))


def eliminar():
    try:
        #producto a eliminar identificado con código 15
        p=(15,)
        consulta="delete from productos where proCodigo=%s"
        resultado=cursor.execute(consulta,p)
        miConexion.commit()
        if (cursor.rowcount==1):
            print("Producto eliminado correctamente")
        else:
            print("No existe producto con ese código")
    except miConexion.Error as e:
        miConexion.rollback()
        print(str(e))


def agregarVarios():
    try:
        #se agregan varios productos de una lista en una sola operación
        productos=[(18, "Zapatillas", 250000, "Calzado"),
                   (19, "Pantalones", 300000, "Ropa"),
                   (20, "Pantalón de cuero", 4500000, "Ropa")]
        consulta = "insert into productos values(null, %s,%s,%s,%s)"
        cursor.executemany(consulta, productos)
        miConexion.commit()
        if (cursor.rowcount==len(productos)):
            print("Productos agregados correctamente")
    except miConexion.Error as e:
        miConexion.rollback()
        print(str(e))
