# This is a python script for a simple multi-threaded proxy server
# It is a simple implementation of a proxy server that can handle multiple
# clients at the same time. It is not a robust implementation and does not
# handle all possible errors. It is meant to be used as a starting point
# for students to build their own proxy server.

import socket, sys, threading, time, os, re, select, signal, errno
from urlparse import urlparse
from SocketServer import ThreadingMixIn

# Global variables