import sqlite3


#Database Connection
conn = sqlite3.connect('intern.db')

#Cursor
c = conn.cursor()

#Drop Table
# c.execute("DROP TABLE movies")
# conn.commit()

#Create Table
# c.execute("""CREATE TABLE movies (
#         movie text,
#         actor text,
#         actress text,
#         director text,
#         release integer
#     )""")
# conn.commit()
# conn.close()


#Add a New Reecord To The Table
def add_one(movie,actor,actress,director,release):
    conn = sqlite3.connect('intern.db')
    c=conn.cursor()
    c.execute("INSERT INTO movies VALUES(?,?,?,?,?)",(movie,actor,actress,director,release))
    conn.commit()
    conn.close()

#Add Many Records TO Table
def add_many(list):
    conn = sqlite3.connect('intern.db')
    c=conn.cursor()
    c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)",(list))
    conn.commit()
    conn.close()


#Query the DB and Return All Records
def show_all():
    #Connect to Database and creat a cursor
    conn = sqlite3.connect('intern.db')
    c=conn.cursor()

    #Query The Database
    c.execute("SELECT rowid,*FROM movies")
    items = c.fetchall()

    for item in items:
        print (item)
    conn.commit()
    conn.close()

#Lookup 
def actor_lookup(actor):
        conn = sqlite3.connect('intern.db')
        c=conn.cursor()

        c.execute("SELECT rowid, * from movies WHERE actor = (?)", (actor,))


        items = c.fetchall()

        for item in items:
            print (item)

        conn.commit()
        conn.close() 