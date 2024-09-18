import mysql.connector
from mysql.connector import Error

class Usuario:
    def __init__(self, id_usuario, correo, contrasenia, nombre, apellido, telefono, rango):
        self.id_usuario = id_usuario
        self.correo = correo
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.rango = rango
        
class Clase:
    def __init__(self, id_clase, nombre_clase, dia_clase, cupo, descripcion=None):
        self.id_clase = id_clase
        self.nombre_clase = nombre_clase
        self.dia_clase = dia_clase
        self.cupo = cupo
        self.descripcion = descripcion

class UsuarioClase:
    def __init__(self, id_usuario, id_clase):
        self.id_usuario = id_usuario
        self.id_clase = id_clase

# Función para conectar a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='emanuel753',
            database='gymbro'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Función para obtener todos los usuarios
def get_usuarios():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            rows = cursor.fetchall()
            usuarios = [Usuario(**row) for row in rows]
            return usuarios
        except Error as e:
            print(f"Error al obtener usuarios: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para obtener todas las clases
def get_clases():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # Modificar la consulta SQL para seleccionar solo las columnas requeridas
            cursor.execute("SELECT id_clase, nombre_clase, dia_clase, cupo FROM clase")
            rows = cursor.fetchall()
            print("Datos obtenidos de la consulta:", rows)  # Imprime los datos para depuración
            if rows:
                clases = [Clase(**row) for row in rows]
                return clases
            else:
                print("No se encontraron clases.")
                return []
        except Error as e:
            print(f"Error al obtener clases: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("No se pudo conectar a la base de datos.")
        return None

# Función para obtener todas las asignaciones de usuario a clase
def get_usuario_clase():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuario_clase")
            rows = cursor.fetchall()
            usuario_clases = [UsuarioClase(**row) for row in rows]
            return usuario_clases
        except Error as e:
            print(f"Error al obtener asignaciones: {e}")
        finally:
            cursor.close()
            connection.close()

# Ejemplo de uso
if __name__ == "__main__":
    usuarios = get_usuarios()
    clases = get_clases()
    usuario_clases = get_usuario_clase()

    print("Usuarios:")
    for usuario in usuarios:
        print(vars(usuario))

    print("\nClases:")
    for clase in clases:
        print(vars(clase))

    print("\nAsignaciones de Usuario a Clase:")
    for uc in usuario_clases:
        print(vars(uc))
