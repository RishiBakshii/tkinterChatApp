import socket
import threading
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000

server.bind((ip_address,port))
server.listen()

clients=[]
nicknames=[]

def client_thread(conn,nickname):
    conn.send(f"{nickname} welcome to this chatapp".encode("utf-8"))

    while True:
        try:
            msg=conn.recv(2048).decode("utf-8")
            if msg:
                print(msg)
            else:
                remove(conn)
        except:
            continue


def broadcast(msg,conn):
    for client in clients:
        if client!=conn:
            try:
                client.send(msg.encode("utf-8"))
            except:
                remove(client)

def remove(conn):
    if conn in clients:
        clients.remove(conn)


while True:
    conn,addr=server.accept()
    conn.send("NICKNAME".encode("utf-8"))
    nickname=conn.recv(2048).decode("utf-8")

    nicknames.append(nickname)
    msg=f"{nickname} has joined"
    print(msg)

    broadcast(msg,conn)

    clients.append(conn)

    threading.Thread(target=client_thread,args=(conn,nickname)).start()

