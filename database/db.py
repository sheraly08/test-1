import sqlite3
from database import queries

path_db = "database/cafe.db"

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.products_table)
    conn.commit()
    conn.close()
    print("DB connect")

def add_product_db(name, price, description):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name, price, description))
    
    conn.commit()
    conn.close()

def get_products_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(queries.select_product)
    products = cursor.fetchall()

    conn.close()

    return products