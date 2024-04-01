# Chat Application Using Tkinter, Socket and Thread
# Author:  Ankan Ghosh | 81.3.24 | Oasis Infobyte Task 2

import socket
import threading

HOST = '127.0.0.1' #local host
PORT = 1234 #can use any port between 0 to 65534
LISTENER_LIMIT = 5
active_clients = [] # List of all currently connected users


#funtion to listen for upcoming messages to all clients
def listen_for_messages(client,username):

    while 1:
    
        message = client.recv(2048).decode('utf-8')
        if message !='': 
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message send from client {username} is empty")


# Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())
      

# Function to send message to all the clients 
def send_messages_to_all(message):
    
    for user in active_clients:

        send_message_to_client(user[1], message)
    
#function to handle client
def client_handler(client):
    
    #server will listen for client message that contain the username
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username,client))
            prompt_message = "SERVER ~ " + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is Empty!")

    threading.Thread(target= listen_for_messages,args=(client,username, )).start()
def main():
    #creating socket class object
    #AF_INET : IPv4 Address family || SOCK_STREAM : TCP 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        server.bind((HOST,PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")
   
    server.listen(LISTENER_LIMIT)

    while 1:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()

if __name__ == '__main__':
    main()


