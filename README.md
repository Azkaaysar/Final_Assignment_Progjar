# Final_Assignment_Progjar
Report:
# Client
The provided code implements a basic client for a remote file management system using XML-RPC in Python. Here's a breakdown of the code and its functionality:
1. The code starts by importing the necessary module `xmlrpc.client`, which is used to create a connection to the XML-RPC server.
2. The `print_menu()` function displays a menu with options for file management operations.
3. The `get_user_input()` function prompts the user for input and returns the input value.
4. The `call_server()` function is responsible for making RPC calls to the server. It takes a method name and optional arguments, creates a connection to the server using `ServerProxy`, and attempts to invoke the specified method with the provided arguments. It also handles various exceptions that might occur during the RPC call, such as XML-RPC faults, connection errors, protocol errors, and general exceptions. Appropriate error messages are printed for each type of exception.
5. The `create_file()`, `read_file()`, `update_file()`, `delete_file()`, and `list_files()` functions implement the respective file management operations. They interact with the server by calling the `call_server()` function with the appropriate method name and arguments. Based on the response received from the server, they display success or failure messages to the user.
6. The `main()` function is the entry point of the program. It runs in a loop and repeatedly displays the menu, prompts the user for a choice, and performs the corresponding file management operation based on the choice. The loop continues until the user chooses to exit.
7. Finally, the `if __name__ == "__main__":` block ensures that the `main()` function is only executed when the script is run directly and not when it is imported as a module.
Overall, the code provides a basic command-line interface for interacting with the remote file management system. Users can choose different operations such as creating, reading, updating, and deleting files, as well as listing all files in the system. Error handling is implemented to catch and handle various exceptions that might occur during the RPC calls.

# Server
The provided code implements a server for a remote file management system using XML-RPC in Python. The code begins by importing the necessary modules: `os` for file system operations and `SimpleXMLRPCServer` for creating an XML-RPC server.
Next, the code defines a class called `RemoteFileManager`, which contains methods for various file management operations. The `create_file` method takes a `filename` and `content` as parameters, and creates a new file with the given name and content by opening the file in write mode and writing the content to it. It returns `True` to indicate successful file creation.
The `read_file` method takes a `filename` as a parameter, opens the file in read mode, and reads its content. It returns the content as a string.
The `update_file` method takes a `filename` and `content` as parameters, opens the file in write mode, and overwrites its content with the new content provided. It also returns `True` to indicate successful file update.
The `delete_file` method takes a `filename` as a parameter and uses the `os.remove()` function to delete the file. It returns `True` to indicate successful file deletion.
The `list_files` method uses the `os.listdir()` function to list all the files in the current directory and returns the list of files.
After defining the `RemoteFileManager` class, the code creates an instance of `SimpleXMLRPCServer` on the specified host and port. It then registers an instance of the `RemoteFileManager` class with the server. This allows the server to expose the methods of the `RemoteFileManager` class for remote procedure calls.
Finally, the server is started by calling `server.serve_forever()`. It listens for incoming XML-RPC requests and handles them accordingly. The server runs indefinitely until it is manually stopped.
Overall, this code provides a simple and functional implementation of a server for a remote file management system using XML-RPC in Python. It allows clients to remotely create, read, update, delete, and list files on the server.
