import socketserver
import http.server

PORT = 8000
# handle the requests
Handsy = http.server.SimpleHTTPRequestHandler
# set up simple HTTP Daemon
httpd = socketserver.TCPServer(("", PORT), Handsy )
# serve the directory to the correct port
httpd.serve_forever()