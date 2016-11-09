import web
import model
import time


urls = (
	'/', 'Index',
	'/browse', 'browsecases',
	'/search(.*)', 'search',
	'/case(.*)', 'case',
	'/new', 'new',
	'/open', 'change_open',
	'/close', 'change_close',	
)


app = web.application(urls, globals())

db = web.database(dbn='sqlite', db='database.db')

render = web.template.render('templates/', base='layout')
case_render = web.template.render('templates/')

class Index(object):
	def GET(self):
		""" Show Page"""
		cases = model.open_cases()
		return render.view_open(cases)


class browsecases(object):
	def GET(self):
		allcases = model.all_cases()
		return render.view_all(allcases)

class search(object):
	def GET(self, search):
		string = web.input()
		result = model.searchs(string.search)
		return render.view_results(result)
		model.drop_vtable()

class case(object):
	def GET(self, case):
		case_n = web.input()
		casen = model.view_print(case_n.case)
		full_case = model.view_print_fill(case_n.case)
		return case_render.view_case(casen, full_case)

class new(object):
	def GET(self):
		today = time.strftime("%d.%m.%Y")
		return render.new(today)

	def POST(self):
		i = web.input()
		n = db.insert('Saker', Fornavn=i.fornavn, Etternavn=i.etternavn, Telefon=i.telefon, Epost=i.email, dato_inn=i.dato_inn, Merke=i.merke, Modell=i.modell, Serienr=i.serienr, Utstyr=i.utstyr, Backup=i.backup, Feilbeskrivelse=i.feilbeskrivelse, Kjøpsdato=i.kjøpsdato, Bongnr=i.bongnr, Garanti=i.garanti, Reklamasjon=i.reklamasjon, mottatt_av=i.mottatt_av, open='Åpen')
		raise web.seeother('/')

class change_close(object):
	def GET(case):
		i = web.input()
		today = time.strftime("%d.%m.%Y")
		c = db.update('Saker', where="Id=$i.case", vars=locals(), open="Stengt", dato_ferdig=today)
		raise web.seeother('/browse')

class change_open(object):
	def GET(case):
		i = web.input()
		c = db.update('Saker', where="Id=$i.case", vars=locals(), open="Åpen")
		raise web.seeother('/')




if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()