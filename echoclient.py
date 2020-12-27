#!/usr/bin/env python3
# Python program to implement client side of chat room.
import socket
import select
import sys


username = input("Enter username:")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 3:
#     print ("Correct usage: script, IP address, port number")
#     exit()
IP_address = '127.0.0.1'
Port = 1237
client.connect((IP_address, Port))
client.send(bytes(username, 'utf-8'))
client.setblocking(False)
# while True:

#     # maintains a list of possible input streams
#     sockets_list = [server]

#     """ There are two possible input situations. Either the  
#     user wants to give manual input to send to other people,  
#     or the server is sending a message to be printed on the  
#     screen. Select returns from sockets_list, the stream that  
#     is reader for input. So for example, if the server wants  
#     to send a message, then the if condition will hold true  
#     below.If the user wants to send a message, the else  
#     condition will evaluate as true"""
#     read_sockets, write_socket, error_socket = select.select(
#         sockets_list, [], [])

#     for socks in read_sockets:
#         if socks == server:
#             message = socks.recv(2048).decode('utf-8')
#             print (message)
#             print("hereServer")
#         else:
#             message = input(f"{username}>")
#             server.send(bytes(message, 'utf-8'))
#             print("here")
            
# server.close()

while True:

    # Wait for user to input a message
    # message = input(f'{username} > ')

    # # If message is not empty - send it
    # if message:

    #     # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
    #     message = message.encode('utf-8')    
    #     client.send(message)

    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:

            # Receive our "header" containing username length, it's size is defined and constant
            # username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            # if not len(username_header):
            #     print('Connection closed by the server')
            #     sys.exit()

            # Convert header to int value
            # username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(1024).decode('utf-8')

            # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
            # message_header = client_socket.recv(HEADER_LENGTH)
            # message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(1024).decode('utf-8')

            # Print message
            print(f'{username} > {message}')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is going to be raised
        # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
        # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
        # If we got different error code - something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
