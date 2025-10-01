import http.server
import socketserver
import platform
import psutil

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Collect system info
            specs = {
                "System": platform.system(),
                "Node Name": platform.node(),
                "Release": platform.release(),
                "Version": platform.version(),
                "Machine": platform.machine(),
                "Processor": platform.processor(),
                "CPU Cores (Physical)": psutil.cpu_count(logical=False),
                "CPU Threads (Logical)": psutil.cpu_count(logical=True),
                "RAM (Total)": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
            }

            # Build HTML page
            html = """
            <html>
            <head>
                <title>Device Specifications</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; background: #eef2f3; }
                    h1 { color: #222; }
                    table { border-collapse: collapse; width: 60%; }
                    th, td { border: 1px solid #444; padding: 8px; text-align: left; }
                    th { background-color: #222; color: white; }
                    tr:nth-child(even) { background-color: #ddd; }
                </style>
            </head>
            <body>
                <h1>Device Specifications</h1>
                <table>
                    <tr><th>Property</th><th>Value</th></tr>
            """
            for key, value in specs.items():
                html += f"<tr><td>{key}</td><td>{value}</td></tr>"
            html += """
                </table>
            </body>
            </html>
            """

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            super().do_GET()

# Start server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://127.0.0.1:{PORT}")
    httpd.serve_forever()