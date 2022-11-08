import sqlite3

def conectar():
    conn=sqlite3.connect("act5/datos.db")
    return conn