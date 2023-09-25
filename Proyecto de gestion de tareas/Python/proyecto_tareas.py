import sqlite3


conn = sqlite3.connect("Proyecto de gestion de tareas.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas(
        TareaID INTEGER PRIMARY KEY,
        Actividad TEXT,
        Vencimiento DATE,
        Completado TEXT
    )
''')
conn.commit()

def agregar_tarea(Actividad, Vencimiento, Completado):
    cursor.execute('''
        INSERT INTO Tareas(Actividad, Vencimiento, Completado) 
        VALUES(?,?,?)
    ''', (Actividad, Vencimiento, Completado))
    conn.commit()
    
def visualizar_tareas():
    cursor.execute('SELECT * FROM tareas')
    Tareas = cursor.fetchall()
    for tarea in Tareas:
        print(tarea)
        
def modificar_tarea(TareaID, Actividad, Vencimiento, Completado):
    cursor.execute('''
        UPDATE Tareas
        SET Actividad = ?, Vencimiento = ?, Completado = ?
        WHERE TareaID = ?
        ''',(Actividad, Vencimiento, Completado, TareaID)) 
    conn.commit()
    
def eliminar_tarea(TareaID):
    cursor.execute('DELETE FROM Tareas WHERE TareaID = ?', (TareaID))
    conn.commit()
    
if __name__ == "__main__":
    while True:
        print("\n1. Agragar tarea")
        print("2. Vizualizar tarea")
        print("3. Modificar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Seleccione opcion: ")
        
        if opcion == "1":
            Actividad = input("Nombre de tarea: ")
            Vencimiento = input("Ingrese fecha de vencimiento (AAAA-MM-DD): ")
            Completado = input("Ya hiciste esta actividad? (si/no): ")
            agregar_tarea(Actividad,Vencimiento)
        elif opcion == "2":
            visualizar_tareas()
        elif opcion == "3":
            TareaID = input("Ingrese el ID de la tarea que desea modificar: ")
            Actividad = input("Nuevo nombre de tarea:")
            Vencimiento = input("Nueva fecha de vencimiento (AAAA-MM-DD): ")
            Completado = input("¿La tarea esta completa? (si/no): ")
            modificar_tarea(TareaID,Actividad,Vencimiento,Completado)
        elif opcion == "4":
            TareaID = input("Ingrese el ID de la tarea que desea eliminar: ")
            eliminar_tarea(TareaID)
        elif opcion == "5":
            break
        
conn.close()
