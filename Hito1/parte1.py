import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect('base.db')
    print("Connection is established: Database is created in memory")
except Error:
    print(Error)

def crud(con):
        while True:
            def crearTabla(con):
                cursorObj.execute("drop table if exists cliente")
                cursorObj.execute(
                    "Create table cliente(id integer, nombre text, apellido1 text, apellido2 text, ciudad text)")
                con.commit()
            print("========================")
            print("  BIENVENIDO AL GESTOR  ")
            print("========================")
            print("[1] Listar clientes     ")
            print("[2] Añadir cliente      ")
            print("[3] Modificar cliente   ")
            print("[4] Borrar cliente      ")
            print("[5] Salir               ")
            print("========================")

            option = input("> ")
            if option == '1':
                cursorObj = con.cursor()
                cursorObj.execute('SELECT * FROM cliente')
                rows = cursorObj.fetchall()
                for row in rows:
                    print(row)

            if option == '2':
                print("Nombre -")
                nombre = input()
                print("Primer Apellido -")
                apellido1= input()
                print("Segundo Apellido -")
                apellido2 = input()
                print("Ciudad -")
                ciudad = input()
                datos = (nombre, apellido1, apellido2, ciudad)
                cursorObj = con.cursor()
                cursorObj.execute('INSERT INTO cliente(nombre, apellido1, apellido2, ciudad) VALUES(?, ?, ?, ?)', datos)
                con.commit()

            if option == '3':
                cursorObj = con.cursor()
                print("Que id quieres modificar")
                numero0 = input()
                print("Que quieres modificar")
                print("[1] nombre")
                print("[2] primer apellido")
                print("[3] segundo apellido")
                print("[4] ciudad")
                numero2=input()

                if numero2 == '1':
                    print("dime el nombre nuevo")
                    nombre_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET nombre =? where id = ?;',(nombre_nuevo, numero0))
                elif numero2 =='2':
                    print("dime el primer apellido nuevo")
                    apellido1_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET apellido1 =? where id = ?;',(apellido1_nuevo, numero0))
                elif numero2 == '3':
                    print("dime el segundo apellido nuevo")
                    apellido2_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET apellido2 =? where id = ?;',(apellido2_nuevo, numero0))
                elif numero2 == '4':
                    print("dime la ciudad nuevo")
                    ciudad_nuevo = input()
                    cursorObj.execute('UPDATE cliente SET ciudad =? where id = ?;',(ciudad_nuevo, numero0))
                else:
                    print("numero no valido")
                con.commit()

            if option == '4':
                cursorObj = con.cursor()
                print("Que id quieres borrar")
                numero0 = input()
                con.execute("DELETE from cliente where id ="+numero0)
                con.commit()

            if option == '5':
                print("Saliendo...\n")
                return False
                break
            input("\nPresiona ENTER para continuar...")
crud(con)
