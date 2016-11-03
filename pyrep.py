import web
import model


urls = (
	'/', 'Index',
	'/browse', 'browsecases',
	'/search(.*)', 'search',
	
)


app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

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




if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()