#!/usr/bin/pyhton3

import http.server
import json
from http import HTTPStatus


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP server request handler.

    This server handles basic GET requests and returns
    different responses based on the requested path.
    """

    def do_GET(self):
        """
        Handles GET requests and returns appropriate responses
        based on the requested path.

        - "/": Returns a plain text welcome message.
        - "/data": Returns a JSON object with sample user data.
        - "/status": Returns a JSON object indicating API status.
        - "/info": Returns a JSON object with API information.
        - Any other path: Returns a 404 JSON error message.
        """
        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))


if __name__ == "__main__":
    HOST, PORT = "", 8000
    server = http.server.HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving on port {PORT}...")
    server.serve_forever()
