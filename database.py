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
#         lead_actor text,
#         actress text,
#         release integer,
#         director text
#     )""")
# conn.commit()
# conn.close()


#Add values
# conn = sqlite3.connect('intern.db')
# c=conn.cursor()
# stuff = [
#             ('Pulp Fiction','John Travolta','Uma Thurman','1994','Quentin Tarantino'),
#             ('The Dark Knight','Christian Bale','Anne Hathaway','2008','Christopher Nolan'),
#             ('Forrest Gump','Tom Hanks','Sally Field','1994','Robert Zemeckis'),
#             ('----- ----','Brad Pitt','Helena Carter','1999','David Fincher'),
#             ('Interstellar','Matthew McConaughey','Anne Hathaway','2014','Christopher Nolan'),
#         ]
# c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)",stuff)
# conn.commit()
# conn.close()


#Add a New Reecord To The Table
def add_one(movie,lead_actor,actress,release,director):
    conn = sqlite3.connect('intern.db')
    c=conn.cursor()
    c.execute("INSERT INTO movies VALUES(?)",(movie,lead_actor,actress,release,director))
    conn.commit()
    conn.close()

#Add Many Records TO Table
# def add_many(list):
#     conn = sqlite3.connect('intern.db')
#     c=conn.cursor()
#     c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)",(list))
#     conn.commit()
#     conn.close()


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

        c.execute("SELECT rowid, * from movies WHERE lead_actor = (?)", (actor,))


        items = c.fetchall()

        for item in items:
            print (item)

        conn.commit()
        conn.close() 