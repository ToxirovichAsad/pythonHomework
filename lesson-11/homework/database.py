import sqlite3


with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Create Table Roster(Name TEXT, Species TEXT, Age INT)')
    cursor.execute('Insert Into Roster Values("Benjamin Sisko", "Human",	40),("Jadzia Dax","Trill",	300),("Kira Nerys",	"Bajoran",	29)')
    

with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Update Roster Set Name = "Ezri Dax" where Name = "Jadzia Dax"')

with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * From Roster Where Species = "Bajoran"')
    

with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Delete From Roster Where Age > 100')

with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    # cursor.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')
    cursor.executescript("""
    UPDATE Roster SET Rank = 'Captain' WHERE name = 'Benjamin Sisko';
    UPDATE Roster SET Rank = 'Lieutenant' WHERE name = 'Ezri Dax';
    UPDATE Roster SET Rank = 'Major' WHERE name = 'Kira Nerys';
""")
with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()
    displayer = cursor.execute('SELECT * FROM Roster Order by Age desc')  
    print(displayer.fetchall())

   




