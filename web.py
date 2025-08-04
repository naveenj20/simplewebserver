from http.server import HTTPServer,BaseHTTPRequestHandler

content="""
<html>
<title>SYSTEM SPECIFICATIONS</title>
<body>
<table border="2" cellspacing="10"cellpadding="6">
<caption>SOFTWARE AND HARDWARE INFORMATION</caption>
<tr>
<th>SNO</th>
<th>specification</th>
<th>value</th>
</tr>
<tr>
<th>1</th>
<th>RAM</th>
<th>16 GB</th>
</tr>
<tr>
<th>2</th>
<th>OS</th>
<th>WINDOWS</th>
</tr>
<tr>
<th>3</th>
<th>PROCESSOR</th>
<th>i5</th>
</tr>
<body>
<html>
"""
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()