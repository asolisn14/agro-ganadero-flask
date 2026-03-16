# models.py
# Operaciones de base de datos

from database import get_connection


def crear_tablas():

    conn = get_connection()
    cursor = conn.cursor()

    # usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # animales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS animales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        identificacion TEXT,
        raza TEXT,
        fecha_nacimiento TEXT,
        sexo TEXT
    )
    """)

    # pesos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pesos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id INTEGER,
        peso REAL,
        fecha TEXT
    )
    """)

    conn.commit()
    conn.close()


# ----------------------
# USUARIOS
# ----------------------

def crear_usuario(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (username,password) VALUES (?,?)",
        (username,password)
    )

    conn.commit()
    conn.close()


def obtener_usuario(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ----------------------
# ANIMALES
# ----------------------

def registrar_animal(usuario_id, identificacion, raza, fecha_nacimiento, sexo):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO animales (usuario_id,identificacion,raza,fecha_nacimiento,sexo)
    VALUES (?,?,?,?,?)
    """,(usuario_id,identificacion,raza,fecha_nacimiento,sexo))

    conn.commit()
    conn.close()


def obtener_animales(usuario_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM animales WHERE usuario_id=?",
        (usuario_id,)
    )

    animales = cursor.fetchall()

    conn.close()

    return animales


def obtener_animal(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM animales WHERE id=?",
        (id,)
    )

    animal = cursor.fetchone()

    conn.close()

    return animal


# ----------------------
# PESOS
# ----------------------

def registrar_peso(animal_id,peso,fecha):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO pesos (animal_id,peso,fecha)
    VALUES (?,?,?)
    """,(animal_id,peso,fecha))

    conn.commit()
    conn.close()


def obtener_pesos(animal_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM pesos
    WHERE animal_id=?
    ORDER BY fecha DESC
    """,(animal_id,))

    pesos = cursor.fetchall()

    conn.close()

    return pesos