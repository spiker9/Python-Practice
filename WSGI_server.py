from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 9998, application)
print("Serving Http on port 9998...")
httpd.serve_forever()