#!/usr/bin/env python3
import sys
import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()

        json_parsed=json.loads(body)        

        print(json.dumps(json_parsed, indent=4, sort_keys=True))

        for node in json_parsed:
            if "type" in node.keys():
                if node["type"]=="Gateway":
                    print(node["mac"])
            if "rssi" in node.keys():
                print(node["mac"] + " : " + str(node["rssi"]))

httpd = HTTPServer(('192.168.100.1', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()
