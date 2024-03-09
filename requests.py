import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
conexion = mysql.connector.connect(
        host=os.getenv("DATABASEHOST"),
        user=os.getenv("DATABASEUSER"),
        password=os.getenv("DATABASEPASSWORD"),
        database=os.getenv("DATABASENAME")
)
def consulta(query):
    cursor = conexion.cursor()
    cursor.execute(query)
    # Obtener todos los resultados
    resultados = cursor.fetchall()
    print("DONE")
    return resultados
def add(query):
    # Ejecutar la consulta
    cursor = conexion.cursor()
    cursor.execute(query)
    # Confirmar la transacción
    conexion.commit()
    print("DONE")
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
def delete(query):
    # Ejecutar la consulta
    cursor = conexion.cursor()
    cursor.execute(query)
    # Confirmar la transacción
    conexion.commit()
    print("DONE")
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()