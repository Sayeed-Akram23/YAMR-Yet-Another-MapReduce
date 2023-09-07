import os
import socket
#client is master_node
#header
SIZE = 1024
FORMAT = "utf"
IP = "127.0.0.1"
PORT = 4456

MASTERNODE_FOLDER = "client_folder" #exists locally
#main function

def main(files,partition):
    # Creating a TCP socket
    master_node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_node.connect((IP, PORT)) #connects using IP address and port number
    # Joining one or more path components
    path = os.path.join(MASTERNODE_FOLDER, files)
    folder = partition #name of folder
    # Sending the folder name
    message = f"{folder}"
    print(f"[master_node] Sending folder name: {folder}")
    master_node.send(message.encode(FORMAT))

    message = master_node.recv(SIZE).decode(FORMAT)
    print(f"[worker_node] {message}\n")
    # File sending phase
    files = sorted(os.listdir(path))
    for file_name in files:
        # sending the file name to worker node
        message = f"FILENAME:{file_name}"
        print(f"[master_node] Sending file name: {file_name}")
        master_node.send(message.encode(FORMAT)) #sends message in encoded format
        message = master_node.recv(SIZE).decode(FORMAT)
        print(f"[worker_node] {message}")

        # Send the data since file till here was empty
        #transferring data!
        file = open(os.path.join(path, file_name), "r")
        file_data = file.read()
        message = f"DATA:{file_data}"
        master_node.send(message.encode(FORMAT)) #sends message in encoded format
        message = master_node.recv(SIZE).decode(FORMAT)
        print(f"[worker_node] {message}")
        # Initiating close command
        message = f"FINISH:Complete data send"
        master_node.send(message.encode(FORMAT))
        message = master_node.recv(SIZE).decode(FORMAT)
        print(f"[worker_node] {message}")

    # Closing the conn from the worker_node
    message = f"CLOSE:File transfer done"
    master_node.send(message.encode(FORMAT)) #sends message
    master_node.close() #terminating connection

if __name__ == "__main__":
    x=int(input("Enter number of partitions: "))
    for i in range (0,x):
    	files="files"+str(i)
    	parti="partition"+str(i)
    	main(files,parti)
    #main("files1","partition1")
    #main("files2","partition2")
