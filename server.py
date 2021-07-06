import socket
import sys

# s = socket.socket()
def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999

        s = socket.socket()

    except socket.error as e:
        print("Socket creation Error: " + e)

def bind_socket():
    try:
        global host
        global port
        global s

        print("binding port: " + str(port))
        print("waiting for connections..")

        s.bind((host, port))

        s.listen(5)

    except socket.error as e:
        print("Got an error, Retrying.." + e)
        bind_socket()

def socket_accept():
    conn, addr = s.accept()
    print("Connection estalished.." + "IP: " + addr[0] + "PORT: " + str(addr[1]))
    send_cmd(conn)
    conn.close()

def send_cmd(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_res = str(conn.recv(1024), "utf-8")
            print(client_res, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
