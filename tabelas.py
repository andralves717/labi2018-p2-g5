import sqlite3 as sql
import sys

def printTable():
	db = sql.connect(database.db)
	
	result = db.execute("SELECT * FROM songs")
	rows = result.fetchall()
	for row in rows:
		print(row)
		
	db.close()
	



musicName
utilizador
votos
excertos
