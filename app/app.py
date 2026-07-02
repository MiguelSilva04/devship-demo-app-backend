from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.environ.get("PORT", 3000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World how are you!\n")

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
