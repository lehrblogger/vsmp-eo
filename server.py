#!/usr/bin/env python
import json
import logging
from optparse import OptionParser
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer

class FrameHandler(SimpleHTTPRequestHandler):
    frame = 1
    last = 1
    log_file = None

    def log_message(self, format, *args):
        if FrameHandler.log_file:
            FrameHandler.log_file.write("%s - - [%s] %s\n" % (self.client_address[0],
                                                              self.log_date_time_string(),
                                                              format%args))
        else:
            SimpleHTTPRequestHandler.log_message(self, format, *args)

    def send_frame_numbers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'current': FrameHandler.frame,
                                     'next'   : FrameHandler.frame + 1}))

    def do_GET(self):
        if self.path == '/increment.json':
            if FrameHandler.frame > FrameHandler.last:
                self.send_error(404, 'Frame {} Not Found'.format(FrameHandler.frame))
            else:
                FrameHandler.frame = FrameHandler.frame + 1
                self.send_frame_numbers()
            return
        if self.path == '/current.json':
            self.send_frame_numbers()
            return
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)


def main():
    usage =  'python server.py -f 1 -l 70000 -p 8000'
    description = 'Turn your Electric Objects EO1 or EO2 into a Very Slow Movie Player.'
    epilog = 'See also https://github.com/lehrblogger/vsmp-eo'

    parser = OptionParser(usage=usage, description=description, epilog=epilog)
    parser.add_option('-f', '--first', dest='first',
                      help='the number of the first frame to display',
                      type='int', default=1)
    parser.add_option('-l', '--last', dest='last',
                      help='the number of the last available frame',
                      type='int')
    parser.add_option('-p', '--port', dest='port',
                      help='the port on which to run the server',
                      type='int', default=8000)
    parser.add_option('-o', '--output', dest='log_file',
                      help='the file to which to write the log output',
                      type='str', default=None)
    (options, args) = parser.parse_args()
    options_ok = True

    if not options.last:
        logging.error('Please specify the last available frame with either "-l" or --last"')
        options_ok = False

    if not options_ok:
        logging.error('See "python server.py --help" for all options.')
    else:
        FrameHandler.frame = options.first
        FrameHandler.last = options.last
        if options.log_file:
            FrameHandler.log_file = open(options.log_file, 'a', 0)
        Handler = FrameHandler
        httpd = SocketServer.TCPServer(('', options.port), Handler)
        httpd.serve_forever()


if __name__ == '__main__':
    main()
