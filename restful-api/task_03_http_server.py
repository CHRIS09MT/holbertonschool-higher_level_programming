from http.server import HTTPServer, BaseHTTPRequestHandler
import json

"""
Simple HTTP server
"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Handles HTTP GET requests, providing responses for specific endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests for /data and /status endpoints.
        """
        
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
  
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            data = {"name": "Jhon", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """
    Starts the HTTP server on port 8000 and listens for requests.
    """

    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()


run()
