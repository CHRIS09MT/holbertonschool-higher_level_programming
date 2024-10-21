from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleBaseHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        routes = {
            '/data': lambda: self.send_json_response({"name": "John", "age": 30, "city": "New York"}),
            '/status': lambda: self.send_text_response("OK"),
            '/info': lambda: self.send_json_response({"version": "1.0", "description": "A simple API built with http.server"}),
            '/': lambda: self.send_text_response("Hello, this is a simple API!", content_type="text/html"),
            }
        
        handler = routes.get(self.path)
        if handler:
            handler()
        else:
            error_message = f"404 Not Found: {self.path}"
            self.send_text_response(error_message, status=404, content_type="text/html")


 

def run(server_class=HTTPServer, handler_class=SimpleBaseHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()
if __name__ == '__main__':
    run()