import socket
    
def send(msg, client_socket):
    msg_Bytes = msg.encode('utf-8')
    msg_len_Decimal = len(msg)
    msg_len_Bytes = str(msg_len_Decimal).encode('utf-8')
    msg_len_Bytes += b' ' * (64-len(msg_len_Bytes))
    client_socket.send(msg_len_Bytes)
    client_socket.send(msg_Bytes)
    
def recv_msg(conxn):
    msg_len = conxn.recv(64).decode('utf-8')
    if msg_len:
        msg_len = int(msg_len)
        msg = conxn.recv(msg_len).decode('utf-8')
        return msg

def chatapp():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('server_ip_addr', 5050))
    send("Hello, World!", client_socket)
    print(f"[FROM SERVER] {recv_msg(client_socket)}")
    send("!DISCONNECTED", client_socket)
    print(f"[FROM SERVER] {recv_msg(client_socket)}")
    
if __name__ == "__main__":
    chatapp()
