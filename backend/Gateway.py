from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import html
import requests


class APIGateway(SimpleHTTPRequestHandler):
    registry_url = "http://localhost:8003"
    
    def get_service_url(self, service_name):
        # Query the registry for the service URL
        try:
            payload = json.dumps({"name": service_name})
            # print(payload)
            response = requests.request("GET", f"{self.registry_url}/services", data=payload)
            service_url = json.loads(response.content)["url"] + service_name
            if response.status_code == 200:
                return service_url # Assuming the registry returns the URL as plain text
            else:
                print(f"Error retrieving URL for {service_name}: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error communicating with registry: {e}")
            return None

    def forward_request(self, service_url):
        content_length = int(self.headers['Content-Length'])
        if content_length > 0:
            body = self.rfile.read(content_length)
        else:
            body = None
        # Forward the request to the specified service
        try:
            response = requests.request(self.command, service_url, data = body)
            response_body = response.content

            # Determine the desired response format from the client's Accept header
            accept_header = self.headers.get('Accept')
            if accept_header == 'application/json':
                # Convert response to JSON
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                json_response = json.dumps({'response': response_body.decode()})
                self.wfile.write(json_response.encode())
            elif accept_header == 'text/html':
                # Convert response to HTML
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                render_response = requests.request("GET", service_url)
                html_response = render_response.text
                html_response = html.escape(response_body.decode())
                self.wfile.write(f"<html><body>{html_response}</body></html>".encode())
            else:
                # Default to plain text
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(response_body)
        except requests.RequestException as e:
            # Handle any exceptions (e.g., service not reachable)
            self.send_error(500, f"Error communicating with service: {e}")


    def do_GET(self):
        # Example routing based on path
        # path = self.path
        service_url = self.get_service_url(self.path)
        if service_url:
            self.forward_request(service_url)
        # if path.startswith("/service1"):
        #     service_url = self.get_service_url("service1")
        #     if service_url:
        #         self.forward_request(service_url, path)
        #     else:
        #         self.send_error(500, "Service URL not found for service1")
        # elif path.startswith("/service2"):
        #     service_url = self.get_service_url("service2")
        #     if service_url:
        #         self.forward_request(service_url, path)
        #     else:
        #         self.send_error(500, "Service URL not found for service2")
        else:
            self.send_error(404, "Service not found")

if __name__ == "__main__":
    # Set up and start the API Gateway
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, APIGateway)
    print(f"API Gateway running on port {port}...")
    httpd.serve_forever()
