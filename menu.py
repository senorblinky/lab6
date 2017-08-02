#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql

#code goes here

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM systems;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games WHERE systemID = 1;""")	
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1	
	db.close()

def fourQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games WHERE systemID = 2;""")	
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1	
	db.close()

def fiveQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games WHERE systemID = 3;""")	
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1	
	db.close()

def sixQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games WHERE systemID = 4;""")	
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1	
	db.close()

def sevenQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games WHERE systemID = 5;""")	
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1	
	db.close()

def eightQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="vegeta12",db="videogames")
	db.query("""SELECT * FROM games WHERE gameName LIKE 'legend%';""")	
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1	
	db.close()
	
while buffer:
	print("""
	0.Exit
	1.See Videogame Systems
	2.See All Games
	3.See All PC Games
	4.See all PS4 Games
	5.See all XBox 360 Games
	6.See all Wii games
	7.See all Wii U games
	8.See all Zelda games
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()
	if buffer == 4:
		fourQuery()
	if buffer == 5:
		fiveQuery()
	if buffer == 6:
		sixQuery()
	if buffer == 7:
		sevenQuery()
	if buffer == 8:
		eightQuery()