from wsgiref.util import setup_testing_defaults

def application(environ, start_response):
	setup_testing_defaults(environ)
	start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
	print('**************************')
	return 'abc'