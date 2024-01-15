import socket
import threading

def handle_client(client_socket, username):
    """
    Handle messages from a client.

    :param client_socket: Client socket
    :param username: Username of the client
    """
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            print(f"{username}: {message}")
            
            # Broadcast the message to all clients
            for client, _ in clients:
                if client != client_socket:
                    try:
                        client.send(f"{username}: {message}".encode("utf-8"))
                    except socket.error:
                        # Remove disconnected client
                        remove_client(client)
        except socket.error:
            # Remove disconnected client
            remove_client(client_socket)
            break

def remove_client(client_socket):
    """
    Remove a client from the list.

    :param client_socket: Client socket
    """
    for i, (client, username) in enumerate(clients):
        if client == client_socket:
            print(f"Removing {username}")
            clients.pop(i)
            break

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen(5)

print("Chat server is listening on port 8080")

# List to store connected clients
clients = []

while True:
    client_socket, addr = server.accept()

    # Prompt the user for a username
    client_socket.send("Enter your username: ".encode("utf-8"))
    username = client_socket.recv(1024).decode("utf-8")

    # Add the client to the list
    clients.append((client_socket, username))
    print(f"{username} connected")

    # Start a new thread for the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()
