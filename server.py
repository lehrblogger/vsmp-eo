#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

class FrameHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    frame = 1
    
    def do_GET(self):
        print self.path
        if self.path == '/':
            self.path = '/index.html'
            print FrameHandler.frame
        if self.path.startswith('/current.png'):
            self.path = '/frames/{}.png'.format(FrameHandler.frame)
        if self.path.startswith('/next.png'):
            print FrameHandler.frame
            self.path = '/frames/{}.png'.format(FrameHandler.frame + 1)
            FrameHandler.frame = FrameHandler.frame + 1
        print self.path
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def main():
    FrameHandler.frame = 28450  # TODO make this a command line arg
    Handler = FrameHandler
    httpd = SocketServer.TCPServer(("", 8000), Handler)

    httpd.serve_forever()

if __name__ == "__main__":
    main()
