import json
import http.server
import socketserver
from typing import Tuple
from http import HTTPStatus


class RegistryHandler(http.server.SimpleHTTPRequestHandler):

    registry_dict = {}
    
    # def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
    #     super().__init__(request, client_address, server)

    def parse_json_body(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)

    def do_GET(self):
        if self.path == '/services':
            data = self.parse_json_body()
            if data["name"] not in self.registry_dict:
                self.send_error(HTTPStatus.NOT_FOUND, "Service not found")
            else:
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"url": self.registry_dict[data["name"]]}).encode("utf-8"))
        
        elif self.path == '/all_services':
            # data = self.parse_json_body()
            payload = {}
            for service, url in self.registry_dict.items():
                payload[service] = url
            
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Page not found")

    def do_POST(self):
        if self.path == '/register':
            try:
                data = self.parse_json_body()
                for name in data['name']:
                    self.registry_dict[name] = data['url']
                self.send_response(HTTPStatus.CREATED)
                self.end_headers()
                self.wfile.write(json.dumps({"status":"Success"}).encode("utf-8"))
            except json.JSONDecodeError:
                self.send_error(HTTPStatus.BAD_REQUEST, "Invalid JSON")
            except KeyError:
                self.send_error(HTTPStatus.BAD_REQUEST, "Missing name or info")
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Endpoint not found")

    def do_DELETE(self):
        if self.path == '/deregister':
            data = self.parse_json_body()
            service_name = data["name"]
            if service_name in self.registry_dict:
                del self.registry_dict[service_name]
                self.send_response(HTTPStatus.OK)
                self.end_headers()
                self.wfile.write(json.dumps({"status":"Success"}).encode("utf-8"))
            else:
                self.send_error(HTTPStatus.NOT_FOUND, "Service not found")
        else:
            self.send_error(HTTPStatus.NOT_FOUND, "Endpoint not found")


if __name__ == "__main__":
    PORT = 8003
    my_server = socketserver.TCPServer(("0.0.0.0", PORT), RegistryHandler)
    print(f"Server started at {PORT}")
    my_server.serve_forever()
