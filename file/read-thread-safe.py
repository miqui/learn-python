import threading

class ThreadSafeFileOperation:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock = threading.Lock()
    
    def write_data(self, data):
        with self.lock:
            with open(self.file_name, 'a') as file:
                file.write(data + '\n')
    
    def read_data(self):
        with self.lock:
            with open(self.file_name, 'r') as file:
                return file.read()

# Example usage
file_op = ThreadSafeFileOperation('example.txt')

# Suppose these operations are performed in different threads
file_op.write_data('Hello from Thread 1')
file_op.write_data('Hello from Thread 2')
