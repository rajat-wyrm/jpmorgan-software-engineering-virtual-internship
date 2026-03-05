import socket
import threading
import time
import random
from datetime import datetime

class StockDataServer:
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []
        self.stock_symbols = ['JPM', 'GS', 'MS', 'BAC', 'C']
        self.running = False
        
    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        print(f"Server started on {self.host}:{self.port}")
        threading.Thread(target=self.accept_clients, daemon=True).start()
        threading.Thread(target=self.broadcast_data, daemon=True).start()
        
    def accept_clients(self):
        while self.running:
            try:
                client, addr = self.server_socket.accept()
                self.clients.append(client)
                print(f"Client connected: {addr}")
            except: break
                
    def generate_data(self):
        data = []
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for sym in self.stock_symbols:
            data.append(f"{ts},{sym},{random.uniform(100,200):.2f},{random.randint(1000,10000)},{random.uniform(-5,5):.2f}")
        return "\n".join(data)
        
    def broadcast_data(self):
        while self.running:
            if self.clients:
                data = self.generate_data()
                for client in self.clients[:]:
                    try: client.send(data.encode())
                    except: self.clients.remove(client)
            time.sleep(2)
            
    def stop(self):
        self.running = False
        for c in self.clients: c.close()
        if self.server_socket: self.server_socket.close()
        print("Server stopped")

if __name__ == "__main__":
    server = StockDataServer()
    try:
        server.start()
        input("Press Enter to stop\n")
    finally:
        server.stop()
