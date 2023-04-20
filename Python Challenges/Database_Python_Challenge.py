
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

create_table = """CREATE TABLE Roster (Name TEXT, Species TEXT, IQ TEXT)"""
original_data = (('Jean-Baptiste Zorg', 'human', '122'), ('Korben Dallas', 'Meat Popsicle', '100'), ("Ak'not", "mangalore", "-5") )
cursor.execute(create_table)
cursor.executemany("INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)", original_data)
storage = []
values = cursor.execute("SELECT * FROM Roster")
for i in values:
    storage.append(i)
print(storage)
cursor.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
storage2 = []
values2 = cursor.execute("SELECT * FROM Roster")
for i in values2:
    storage2.append(i)
print(storage2)
conn.commit()
conn.close()

