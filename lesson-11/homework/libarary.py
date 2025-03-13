import sqlite3

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Create Table Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT)')

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Insert Into Books Values ("To Kill a Mockingbird",	"Harper Lee",	1960, "Fiction"),("1984",	"George Orwell",	1949, "Dystopian"),("The Great Gatsby",	"F. Scott Fitzgerald",	1925, "Classic")')

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Update Books Set Year_Published = 1950 Where Title = "1984"')

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    dystopian = cursor.execute('Select * From Books where Genre = "Dystopian"')
    print(dystopian.fetchall())
with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute('Delete From Books Where Year_Published < 1950')

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    cursor.execute('ALTER TABLE Books ADD COLUMN Rating REAL')  
with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()   
    cursor.executescript("""
        UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird';
        UPDATE Books SET Rating = 4.7 WHERE Title = '1984';
        UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby';
    """)

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    named = cursor.execute('Select * From Books order by Year_Published asc')
    print(named.fetchall())
