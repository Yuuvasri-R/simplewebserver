import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Top 5 Revenue Generating Software Companies</title>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; margin-top: 30px; }
                    table { border-collapse: collapse; margin: auto; width: 60%; }
                    th, td { border: 1px solid black; padding: 10px; text-align: center; }
                    th { background-color: #d9d9d9; }
                </style>
            </head>
            <body>
                <h2>Top 5 Revenue Generating Software Companies</h2>
                <table>
                    <tr><th>s.no</th><th>companies</th><th>revenue</th></tr>
                    <tr><td>1</td><td>Microsoft</td><td>65 billion</td></tr>
                    <tr><td>2</td><td>Oracle</td><td>29.6 billion</td></tr>
                    <tr><td>3</td><td>IBM</td><td>29.1 billion</td></tr>
                    <tr><td>4</td><td>SAP</td><td>6.4 billion</td></tr>
                    <tr><td>5</td><td>Symantec</td><td>5.6 billion</td></tr>
                </table>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://127.0.0.1:{PORT}")
    httpd.serve_forever()