
import socket
import threading

# Server IP and port
HOST = '127.0.0.1'  # Change to server's IP if needed
PORT = 12346

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error! Disconnected from server.")
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input('')}"
        client.send(msg.encode('utf-8'))
        print("Sent message:", msg)
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


