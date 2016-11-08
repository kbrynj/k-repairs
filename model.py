import web
import time
import sqlite3



def open_cases():
	con = sqlite3.connect('database.db')
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Saker WHERE open = 'Åpen' ORDER BY Id ASC")
		rows = cur.fetchall()
		return rows


def all_cases():
	con = sqlite3.connect('database.db')
	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM Saker")
		arows = cur.fetchall()
		return arows

def searchs(strng):
	con = sqlite3.connect('database.db')
	with con:		
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS Search;")		
		cur.execute("CREATE VIRTUAL TABLE Search USING fts3(Id TEXT, Fornavn TEXT, Etternavn TEXT, Telefon char(8), Epost TEXT, dato_inn DATE, dato_ferdig DATE, Merke TEXT, Modell TEXT, Serienr varchar(30), Kjøpsdato DATE, Bongnr char(6), Utstyr TEXT, Backup TEXT, Feilbeskrivelse TEXT, Garanti TEXT, Reklamasjon TEXT, mottatt_av TEXT, open INT);")
		cur.execute("INSERT INTO Search SELECT Id, Fornavn, Etternavn, Telefon, Epost, dato_inn, dato_ferdig, Merke, Modell, Serienr, Kjøpsdato, Bongnr, Utstyr, Backup, Feilbeskrivelse, Garanti, Reklamasjon, mottatt_av, open FROM Saker;")
		cur.execute("SELECT * FROM Search WHERE Search MATCH '{st}' ORDER BY dato_inn DESC;".format(st=strng)) 
		result = cur.fetchall()
		return result

def drop_vtable():
	con = sqlite3.connect('database.db')
	with con:
		cur = con.cursor()
		cur.execute("DROP TABLE Search;")


def view_print(casenumber):
	con = sqlite3.connect('database.db')
	with con:		
		cur = con.cursor()
		cur.execute("SELECT * FROM Saker WHERE Id = '{nmbr}';".format(nmbr=casenumber))
		cnumber = cur.fetchall()
		for i in cnumber:
			case_i = i[0]
			return case_i


def view_print_fill(casenumber):
	con = sqlite3.connect('database.db')
	with con:		
		cur = con.cursor()
		cur.execute("SELECT * FROM Saker WHERE Id = '{nmbr}';".format(nmbr=casenumber))
		cnumber = cur.fetchall()
		return cnumber


