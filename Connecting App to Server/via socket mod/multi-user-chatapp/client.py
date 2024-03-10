import socket
import threading

nickname = input('Enter Nickkname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print('An error  occurred!')
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input('')}"
        client.send(msg.encode('ascii'))

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)
receive_thread.start()
write_thread.start()

