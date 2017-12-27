#!/usr/local/bin python3
# encoding: utf-8
__author__ = 'Liangmingli'



import socket
from socketserver import ForkingTCPServer as FTS
import http.server
from http.server import SimpleHTTPRequestHandler as SHRH

class ForkHTTPServer(FTS):
    pass

def test(ServerHandler=SHRH, ServerClass=ForkHTTPServer):
    http.server.test(ServerHandler, ServerClass)

if __name__ == '__main__':
    ip_address = socket.gethostbyname(socket.gethostname())
    print("Server address:[%s]" % ip_address)
    test()
