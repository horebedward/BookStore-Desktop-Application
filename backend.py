import sqlite3


def create_table():
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("CREATE TABLE  IF NOT EXISTS books \
				  (id INTEGER PRIMARY KEY,\
				   title TEXT,year INTEGER,author TEXT,isbn INTEGER)")
	con.commit()
	con.close()

def insert(title,year,author,isbn):
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("INSERT INTO books VALUES(NUll,?,?,?,?)",(title,year,author,isbn))
	con.commit()
	con.close()

def view_all():
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("SELECT * FROM books")
	row = cursor.fetchall()
	con.close()
	return row

def delete(id):
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("DELETE FROM books WHERE id = ?",(id,))
	con.commit()
	con.close()

def update(id,title,year,author,isbn):
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("UPDATE books SET title = ?, \
					year = ?,author = ?,isbn = ? WHERE id = ?" \
					,(title,year,author,isbn,id))
	con.commit()
	con.close()

def search(title = "",year = "",author = "",isbn = ""):
	con = sqlite3.connect('lite.db')
	cursor = con.cursor()
	cursor.execute("SELECT  * FROM books WHERE title=? or year=? \
					or author = ? or isbn = ?",(title,year,author,isbn))
	row = cursor.fetchall()
	con.close()
	return row










