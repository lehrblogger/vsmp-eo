#!/usr/bin/env python
import json
import SimpleHTTPServer
import SocketServer

class FrameHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    frame = 1
    last = 28602
    
    def do_GET(self):
        if self.path == '/increment.json':
            FrameHandler.frame = FrameHandler.frame + 1
            if FrameHandler.frame >= FrameHandler.last:
                self.send_error(404, 'Frame {} Not Found'.format(FrameHandler.frame))
            else:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'current': FrameHandler.frame,
                                             'next'   : FrameHandler.frame + 1}))
            return
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def main():
    FrameHandler.frame = 28450  # TODO make this a command line arg, and get max number too
    Handler = FrameHandler
    httpd = SocketServer.TCPServer(("", 8000), Handler)

    httpd.serve_forever()

if __name__ == "__main__":
    main()
