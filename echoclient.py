#!/usr/bin/env python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = '127.0.0.1'
Port = 1234
client.connect((IP_address, Port))

while True:
    msg = input("Enter msg to echo: ")
    client.sendall(bytes(msg, 'utf-8'))
    echo = client.recv(1024).decode('utf-8')
    print("Echo: ", echo)
