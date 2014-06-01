# -*- encoding: utf-8 -*-

import os
import jinja2
import webapp2
import random


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
            if "all" in let:
                if lenstr >= 1:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(32, 255, 1)
                        if var == 127:
                            var = var-5
                        v.append(unichr(var))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 1 for all characters."
            elif "extra" in let:
                if lenstr >= 1:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(128, 255, 1)
                        v.append(unichr(var))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 1 for extra symbols."
            elif "quotas" in let:
                if lenstr >= 3:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(1, 3, 1)
                        if var == 1:
                            v.append(unichr(34))
                        elif var == 2:
                            v.append(unichr(39))
                        else:
                            v.append(unichr(96))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 3 for quotas symbols."
            elif "simbols" in let:
                if lenstr >= 1:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(32, 126, 1)
                        v.append(unichr(var))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 1 for simbols."
            elif "alpha" in let:
                if lenstr >= 1:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(1, 62, 1)
                        if var <= 10:
                            var = random.randrange(48, 57, 1)
                        elif var <=36:
                            var = random.randrange(65, 90, 1)
                        else:
                            var = random.randrange(97, 122, 1)
                        v.append(unichr(var))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 1 for alphanumerics characters."
            elif "numeric" in let:
                if lenstr >= 1:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(48, 57, 1)
                        v.append(unichr(var))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 1 for numbers."
            else:
                if lenstr >= 1:
                    v = []
                    for i in xrange(lenstr):
                        var = random.randrange(1, 52, 1)
                        if var <=26:
                            var = random.randrange(65, 90, 1)
                        else:
                            var = random.randrange(97, 122, 1)
                        v.append(unichr(var))
                    results = ''.join(v)
                    lenres = len(results)
                else:
                    error = True
                    results = "Minimum length is 1 for letters."

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