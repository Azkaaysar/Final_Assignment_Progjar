import os
from xmlrpc.server import SimpleXMLRPCServer

class RemoteFileManager:
    def create_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        return True

    def read_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content

    def update_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        return True

    def delete_file(self, filename):
        os.remove(filename)
        return True

    def list_files(self):
        files = os.listdir('.')
        return files

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(RemoteFileManager())

# Start the server
print("Server listening on port 8000...")
server.serve_forever()
