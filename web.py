from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
    <title>Top 5 Revenue Generating Software Companies</title>
<body>
    <table border="2" cellspacing='10' cellpadding='6'>
        <caption>Top 5 Revenue Generating Software Companies</caption>
        <tr>
            <th>s.no</th>
            <th>companies</th>
            <th>revenue</th>
        </tr>
        <tr>
            <th>1</th>
            <th>Microsoft</th>
            <th>65 billion</th>
        </tr>
        <tr>
            <th>2</th>
            <th>Oracle</th>
            <th>29.6 billion</th>
        </tr>
        <tr>
            <td>3</td>
            <td>IBM</td>
            <td>29.1 billion</td>
        </tr>
        <tr>
            <th>4</th>
            <th>SAP</th>
            <th>6.4 billion</th>
        </tr>
        <tr>
            <th>5</th>
            <th>Symantec</th>
            <th>5.6 billion</th>
</body>
</html>

"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()