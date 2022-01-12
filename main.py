import database1


#Add a record to the databse
database1.add_one('Inception','Leonardo DiCaprio','Ellen Page','Christopher Nolan','2010')

#Add Many Records
stuff = [
            ('Pulp Fiction','John Travolta','Uma Thurman','Quentin Tarantino','1994'),
            ('The Dark Knight','Christian Bale','Anne Hathaway','Christopher Nolan','2008'),
            ('Forrest Gump','Tom Hanks','Sally Field','Robert Zemeckis','1994'),
            ('----- ----','Brad Pitt','Helena Carter','David Fincher','1999'),
            ('Interstellar','Matthew McConaughey','Anne Hathaway','Christopher Nolan','2014'),
   ]
database1.add_many(stuff)


#Show all records
database1.show_all()

#Lookup Actor Name
database1.actor_lookup("Tom Hanks")

