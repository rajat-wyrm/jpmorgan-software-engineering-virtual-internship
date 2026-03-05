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
        
        print(f"Stock data server started on {self.host}:{self.port}")
        
        accept_thread = threading.Thread(target=self.accept_clients)
        accept_thread.daemon = True
        accept_thread.start()
        
        broadcast_thread = threading.Thread(target=self.broadcast_data)
        broadcast_thread.daemon = True
        broadcast_thread.start()
        
    def accept_clients(self):
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                self.clients.append(client_socket)
                print(f"New client connected: {address}")
                
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()
            except:
                break
                
    def handle_client(self, client_socket, address):
        try:
            while self.running:
                data = client_socket.recv(1024).decode().strip()
                if data:
                    print(f"Received from {address}: {data}")
                    if data.lower() == 'quit':
                        break
        except:
            pass
        finally:
            client_socket.close()
            if client_socket in self.clients:
                self.clients.remove(client_socket)
            print(f"Client disconnected: {address}")
            
    def generate_stock_data(self):
        data = []
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for symbol in self.stock_symbols:
            price = round(random.uniform(100, 200), 2)
            volume = random.randint(1000, 10000)
            change = round(random.uniform(-5, 5), 2)
            
            data.append({
                'timestamp': timestamp,
                'symbol': symbol,
                'price': price,
                'volume': volume,
                'change': change
            })
        return data
        
    def broadcast_data(self):
        while self.running:
            if self.clients:
                stock_data = self.generate_stock_data()
                output = "timestamp,symbol,price,volume,change\n"
                for item in stock_data:
                    output += f"{item['timestamp']},{item['symbol']},{item['price']},{item['volume']},{item['change']}\n"
                
                for client in self.clients[:]:
                    try:
                        client.send(output.encode())
                    except:
                        self.clients.remove(client)
            time.sleep(2)
            
    def stop(self):
        self.running = False
        for client in self.clients:
            try:
                client.close()
            except:
                pass
        if self.server_socket:
            self.server_socket.close()
        print("Server stopped")

if __name__ == "__main__":
    server = StockDataServer()
    try:
        server.start()
        input("Press Enter to stop the server...\n")
    finally:
        server.stop()
