import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 5050))

def send(msg, conxn):
    msg_Bytes = msg.encode('utf-8')
    msg_len_Decimal = len(msg)
    msg_len_Bytes = str(msg_len_Decimal).encode('utf-8')
    msg_len_Bytes += b' ' * (64-len(msg_len_Bytes))
    conxn.send(msg_len_Bytes)
    conxn.send(msg_Bytes)
    
def recv_msg(conxn):
    msg_len = conxn.recv(64).decode('utf-8')            # Blocker: Wait For Msg From Client
    if msg_len:
        msg_len = int(msg_len)
        msg = conxn.recv(msg_len).decode('utf-8')
        return msg

def client_connection_thread(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected!")
    connected = True
    while connected:
        msg = recv_msg(conn)
        if msg == "!DISCONNECTED":
            connected = False
        print(f"[{addr}] {msg}")
        send("Copy that!", conn)
    conn.close()

def start():
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()             # Blocker: Wait For Connections From Client
        thread = threading.Thread(target=client_connection_thread, args=(conn, addr))   # Establish Connection with New Thread to Handler Individual Client
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")

if __name__ == "__main__":
    start()
