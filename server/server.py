#!/usr/bin/env python
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import bitly_api 

class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            html = open('D:\Python\services\server\index.html')
            self.wfile.write(html.read().encode('utf-8')) #cp1251 encode('utf-8')

        elif self.path.endswith(".png"):
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
                
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
            
        elif self.path.endswith(".ico"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
        
        elif self.path.endswith(".css"):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
        
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
                
        elif self.path.endswith(".js"):
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
        
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
            
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        try:
            
            print("POST request, path:", self.path, "body:", body.decode('utf-8'))
            
            if self.path == "/getShortLink":
                
                datas = json.loads(body.decode('utf-8'))
                link = datas['data']        
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                result = getShortLink(link);
                self.wfile.write(result.encode())
                
            else:
                self.send_response(400, 'Bad Request: Method does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
        except Exception as err:
            print("do_POST exception: %s" % str(err))


def main():
    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)


def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
        pass
    httpd.server_close()


def getShortLink(longlink):
    BITLY_ACCESS_TOKEN ="47812d75926cea292d2ef10d25382b5b51af797b"
    access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
    short_url = access.shorten(longlink) 
    print('Short URL = ',short_url['url'])
    return short_url['url']


if __name__ == '__main__':
    main()
