import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

html_page = Path(__file__).parent / "index.html"

PAGE = html_page.read_bytes()


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(PAGE)


def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8347):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Running on 0.0.0.0:{port}")
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()


def main():
    run()


if __name__ == "__main__":
    main()
