#!/usr/bin/env python

import socket
import time
import getopt
import sys
import asyncore
import logging


s_flocklab_url = "whymper.ee.ethz.ch"
s_nodes = "001 002 003 004 006 007 008 010 011 013 014 015 016 017 018 019 020 022 023 024 025 026 027 028 031 032 033 200 201 202 204"
#s_nodes = "001 002"
lst_nodes = [int(s_val) for s_val in s_nodes.split(" ")]
i_port_start = 50100
try:
    opts, args = getopt.getopt(sys.argv[1:], "u:n:p:h", ["flocklab-url=", "nodes=", "port-start=", "help"])

except getopt.GetoptError, err:
    print str(err)
    sys.exit(2)
  
for opt, arg in opts:
    if opt in ('-u', '--flocklab-url'):
        lst_addresses = arg.split(",")
    elif opt in ('-n', '--nodes'):
        lst_times = [int(s_val) for s_val in arg.split(" ")]
    elif opt in ('-p', '--port-start'):
        i_port = int(arg)
    elif opt in ('-h', '--help'):
        show_help(sys.argv[0])
        sys.exit(0)
    else:
        print 'Unknown option'
        sys.exit(1)

for i_node_id in lst_nodes:
    print '----- set node : %03d start ---------' % i_node_id
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(None)
        s.connect((s_flocklab_url, i_port_start + i_node_id))
        s.send('\n\n\nnodeid ' + str(i_node_id) + '\n\n')
        time.sleep(1)
        data = s.recv(1028)
        print data
        s.close()
    except socket.error, err:
        print err
    print '----- set node : %03d end -----------' % i_node_id
    
