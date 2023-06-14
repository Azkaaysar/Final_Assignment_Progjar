import xmlrpc.client

def print_menu():
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. List all files")
    print("6. Exit")

def get_user_input(prompt):
    return input(prompt)

def call_server(method, *args):
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        try:
            result = getattr(proxy, method)(*args)
            return result
        except xmlrpc.client.Fault as err:
            print(f"XML-RPC fault occurred: {err.faultCode} {err.faultString}")
        except ConnectionRefusedError:
            print("Error: Failed to connect to the server.")
        except xmlrpc.client.ProtocolError as err:
            print(f"Error occurred: {err}")
        except Exception as e:
            print(f"Error occurred: {e}")

def create_file():
    filename = get_user_input("Enter the filename: ")
    content = get_user_input("Enter the content: ")
    result = call_server("create_file", filename, content)
    if result:
        print(f"File '{filename}' created successfully.")
    else:
        print(f"Failed to create file '{filename}'.")

def read_file():
    filename = get_user_input("Enter the filename: ")
    content = call_server("read_file", filename)
    if content is not None:
        print(f"Content of file '{filename}': {content}")
    else:
        print(f"File '{filename}' not found.")

def update_file():
    filename = get_user_input("Enter the filename: ")
    content = get_user_input("Enter the updated content: ")
    result = call_server("update_file", filename, content)
    if result:
        print(f"File '{filename}' updated successfully.")
    else:
        print(f"Failed to update file '{filename}'.")

def delete_file():
    filename = get_user_input("Enter the filename: ")
    result = call_server("delete_file", filename)
    if result:
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"Failed to delete file '{filename}'.")

def list_files():
    files = call_server("list_files")
    if files:
        print("Files in the system:")
        for file in files:
            print(file)
    else:
        print("No files found.")

def main():
    while True:
        print_menu()
        choice = get_user_input("Enter your choice: ")
        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            update_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            list_files()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
