import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 5050))

def send(msg, conxn):                               # Function to Encode & Send Message
    msg_Bytes = msg.encode('utf-8')                         # Encode Message to Bytes
    msg_len_Decimal = len(msg)                              # Get Lenght of Message 
    msg_len_Bytes = str(msg_len_Decimal).encode('utf-8')    # Encode the Lenght of Message to Bytes
    msg_len_Bytes += b' ' * (64-len(msg_len_Bytes))         # Padded for Header to Sends
    conxn.send(msg_len_Bytes)                               # Send Encoded Headed
    conxn.send(msg_Bytes)                                   # Send Encoded Message
    
def recv_msg(conxn):
    msg_len = conxn.recv(64).decode('utf-8')        # Blocker: Wait For Header From Client and Decode it
    if msg_len:                                     # Check if Header Length is not Empty
        msg_len = int(msg_len)                          # Convert Header to Interger
        msg = conxn.recv(msg_len).decode('utf-8')       # Blocker: Wait to Recieve Message from Client
        return msg                                      # Return Message

def client_connection_thread(conn, addr):           # Functiont to Handle Clients Connections
    print(f"[NEW CONNECTION] {addr} Connected!")    
    connected = True
    while connected:                             # Infinite Loop
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
