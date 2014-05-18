import os
import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

    def get(self):

        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class GeneratorPage(webapp2.RequestHandler):

    def post(self):

        lenstr = int(self.request.get('lenght'))
        let = self.request.get('typ')
        error = False
        lista = []
        var = 0
        lenres = 0

        # generar ahora toda la cadena con el resto de caracteres
        if "lengtype" in let:
            v = []
            for i in range(lenstr):
                v.append(u"a")
            results = ''.join(v)
            lenres = len(results)
        else:
            if "extra" in let:
                if lenstr >= 132:
                    v = []
                    v.append("aA4#")
                    for i in range(128,256):
                        v.append(unichr(i))
                    if lenstr > 132:
                        for i in range(lenstr-132):
                             v.append('T')
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Length minimun is 132 for extra symbols."
            elif "simbols" in let:
                if lenstr >= 36:
                    v = []
                    v.append("aA4")
                    for i in range(32,48):
                        v.append(unichr(i))
                    for i in range(58,65):
                        v.append(unichr(i))
                    for i in range(91,97):
                        v.append(unichr(i))
                    for i in range(123,127):
                        v.append(unichr(i))
                    if lenstr > 36:
                        for i in range(lenstr-36):
                            v.append('#')
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Length minimun is 36 for simbols."
            elif "numeric" in let:
                if lenstr >= 3:
                    v = []
                    v.append("aA4")
                    if lenstr > 3:
                        for i in range(lenstr-3):
                            v.append('2')
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Length minimun is 3 for numbers."
            else:
                if lenstr >= 2:
                    v = []
                    v.append("aA")
                    if lenstr > 2:
                        for i in range(lenstr-2):
                            v.append('E')
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Length minimun is 2 for letters."

        template_values = {
            'result': results,
            'error': error,
            'lengresult': lenres,
        }

        template = JINJA_ENVIRONMENT.get_template('generator.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/generator', GeneratorPage),
], debug=True)