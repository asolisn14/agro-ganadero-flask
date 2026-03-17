# models.py

from database import conectar


def crear_tablas():

    conn = conectar()
    cursor = conn.cursor()

    # USUARIOS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    # ANIMALES
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

    # PESOS
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


# -------------------
# USUARIOS
# -------------------

def crear_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (username, password)
    VALUES (?,?)
    """, (username, password))

    conn.commit()
    conn.close()


def obtener_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()
    conn.close()
    return user


# -------------------
# ANIMALES
# -------------------

def registrar_animal(usuario_id, identificacion, raza, fecha_nacimiento, sexo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO animales (usuario_id, identificacion, raza, fecha_nacimiento, sexo)
    VALUES (?,?,?,?,?)
    """, (usuario_id, identificacion, raza, fecha_nacimiento, sexo))

    conn.commit()
    conn.close()


def obtener_animales(usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM animales WHERE usuario_id=?
    """, (usuario_id,))

    data = cursor.fetchall()
    conn.close()
    return data


def obtener_animal(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM animales WHERE id=?
    """, (id,))

    data = cursor.fetchone()
    conn.close()
    return data


# -------------------
# PESOS
# -------------------

def registrar_peso(animal_id, peso, fecha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO pesos (animal_id, peso, fecha)
    VALUES (?,?,?)
    """, (animal_id, peso, fecha))

    conn.commit()
    conn.close()


def obtener_pesos(animal_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM pesos WHERE animal_id=?
    """, (animal_id,))

    data = cursor.fetchall()
    conn.close()
    return data