import web
import model


urls = (
	'/', 'Index',
	'/browse', 'browsecases',
	'/search(.*)', 'search',
	'/case(.*)', 'case',
	
)


app = web.application(urls, globals())

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





if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()