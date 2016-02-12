import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8070)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    #message = input("Please choose a file or directory:") = 'This is the message.  It will be repeated.'
    message = ''

    message = raw_input("E for E.txt, D for D.txt, or Q for Q.txt: ")

    if message == 'E':
        E = open('E.txt', 'r')
        #print (sys.stderr, 'requesting "%s"' % message)
        sock.sendall(message)
    elif message == 'D':
        D = open('D.txt', 'r')
        #print (sys.stderr, 'requesting "%s"' % message)
        sock.sendall(message)
    elif message =='Q':
        Q = open('Q.txt', 'r')
        #print (sys.stderr, 'requesting "%s"' % message)
        sock.sendall(message)
    else:
        print "Invalid Option. Exiting..."
    

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print (sys.stderr, 'received "%s"' % data)

finally:
    print (sys.stderr, 'closing socket')
    sock.close()
