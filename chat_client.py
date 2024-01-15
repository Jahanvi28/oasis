import socket
import threading

def receive_messages(client_socket):
    """
    Receive messages from the server.

    :param client_socket: Client socket
    """
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except socket.error:
            print("Disconnected from the server.")
            break

def send_messages(client_socket):
    """
    Send messages to the server.

    :param client_socket: Client socket
    """
    while True:
        message = input()
        client_socket.send(message.encode("utf-8"))

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

# Prompt the user for a username
username = input("Enter your username: ")
client.send(username.encode("utf-8"))

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client,))

receive_thread.start()
send_thread.start()
