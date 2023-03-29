import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 5050))

def client_connection_thread(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected!")
    connected = True
    while connected:
        msg_length = conn.recv(64).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == "!DISCONNECTED":
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()

def start():
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=client_connection_thread, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")

if __name__ == "__main__":
    start()
