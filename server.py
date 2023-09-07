import socket
import os

# Define constants
SIZE = 1024
FORMAT = "utf"
IP = "127.0.0.1"
PORT = 4456
WORKERNODE_FOLDER = "server_folder"  # exists locally

# Main function
def main():
    print("[STARTING] worker_node is starting.\n")
    worker_node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker_node.bind((IP, PORT))
    worker_node.listen()
    print("worker_node is waiting for master_node.")

    while True:
        conn, addr = worker_node.accept()
        print(f"[NEW WORKER NODE CREATED] {addr} connection successful.\n")

        try:
            # Worker node receives the folder_name
            folder = conn.recv(SIZE).decode(FORMAT)

            # Creating the folder
            folder_path = os.path.join(WORKERNODE_FOLDER, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                conn.send(f"Folder ({folder}) created.".encode(FORMAT))
            else:
                conn.send(f"Folder ({folder}) already exists.".encode(FORMAT))

            # Receiving files from master_node
            while True:
                message = conn.recv(SIZE).decode(FORMAT)
                command, msg = message.split(":")
                
                if command == "FILENAME":
                    print(f"[master_node] Received filename: {msg}.")
                    file_path = os.path.join(folder_path, msg)
                    file = open(file_path, "w")
                    conn.send("Filename received.".encode(FORMAT))
                    
                elif command == "DATA":
                    print(f"[master_node] Receiving file data.")
                    file.write(msg)
                    conn.send("File data received".encode(FORMAT))
                    
                elif command == "FINISH":
                    file.close()
                    print(f"[master_node] {msg}.\n")
                    conn.send("The data is saved.".encode(FORMAT))
                    
                elif command == "CLOSE":
                    conn.close()
                    print(f"[master_node] {msg}")
                    break

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    main()
