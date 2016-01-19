#!/usr/bin/env python

# Copyright Nick Zarczynski. 
# https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-2/
# Please don't sue me Nick


import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("",8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()

