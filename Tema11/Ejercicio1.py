import sqlite3

c = sqlite3.connect('app.db')
cursor = c.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS alumnos
          ([id] INTEGER PRIMARY KEY, [nombre] TEXT, [apellido] TEXT)
          ''')
c.execute('''
          INSERT INTO alumnos (id, nombre, apellido)
                VALUES
                (1,'Diego', 'Perez'),
                (2,'Test', 'Apellido2'),
                (3,'Romina', 'Mena'),
                (4,'Valentina', 'Londra'),
                (5,'Ema', 'Josua'),
                (6,'Luis', 'Otero'),
                (7,'Paz', 'Martin'),
                (8,'Alberto', 'Juarez') 
          ''')
c.commit()

rows = cursor.execute('SELECT * FROM alumnos WHERE nombre="Diego"')
for row in rows:
    print(row)

cursor.close()
c.close()