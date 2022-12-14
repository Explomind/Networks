import socket
import threading

def broadcast(msg):
    for user_sock in users.keys():
        user_sock.send(msg)

def working(user_sock):
    while True:
        try:
            inp_msg = user_sock.recv(1024)
            broadcast(inp_msg)
        except:
            left_user = users[user_sock]
            del users[user_sock]
            broadcast(f"{left_user} has left.".encode("ascii"))
            user_sock.close()
            break

def receiving():
    while True:
        user_sock, user_address = s.accept()
        print(f"Connected by {user_address}")

        user_sock.send("NICK".encode("ascii"))
        new_nick = user_sock.recv(1024).decode("ascii")
        users[user_sock] = new_nick
        print(users)

        print(f"Nick: {users[user_sock]}")
        user_sock.send(f"You are connected to server".encode("ascii"))
        broadcast(f"{new_nick} is joined.".encode("ascii"))

        thread = threading.Thread(target=working, args=(user_sock,))
        thread.start()

HOST = "127.0.0.1"
PORT = 55555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
users = {}  #dict with users' sockets and nicknames
print("Server is working...")
receiving()
