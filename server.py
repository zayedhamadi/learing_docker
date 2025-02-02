from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, My name is Hamadi Zayed, I am trying to learn  Docker!")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serveur démarré sur le port {PORT}")
    httpd.serve_forever()
