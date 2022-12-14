import socket
import threading

def receiving():
    while True:
        data_chunk = sock.recv(1024)
        if data_chunk:
            print(data_chunk)

# def send_msg():
#     # while True:
#         msg_out = input()
#         if msg_out == "quit":
#             sock.close()
#         sock.send(msg_out.encode('ascii'))

HOST = "127.0.0.1"
PORT = 65432

sock = socket.socket()
sock.connect((HOST, PORT))
nickname = input("Your nickname: ")
sock.send(nickname.encode('ascii'))
# sock.send(nickname)

rec_thread = threading.Thread(target=receiving)
rec_thread.start()

# send_thread = threading.Thread(target=send_msg)
# send_thread.start()

while True:
    msg_out = input()
    if msg_out == "quit":
        break
    sock.send(msg_out.encode('ascii'))
    # sock.send(msg_out)

sock.close()
