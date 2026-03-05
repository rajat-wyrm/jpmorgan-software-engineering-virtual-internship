import socket
import threading
import csv
import time

class StockDataClient:
    def __init__(self, host='localhost', port=9999):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.data_buffer = []
        
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.running = True
            print(f"Connected to server at {self.host}:{self.port}")
            
            receive_thread = threading.Thread(target=self.receive_data)
            receive_thread.daemon = True
            receive_thread.start()
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
            
    def receive_data(self):
        buffer = ""
        while self.running:
            try:
                data = self.socket.recv(4096).decode()
                if not data:
                    break
                    
                buffer += data
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    if line.strip() and not line.startswith('timestamp'):
                        self.process_data(line)
            except:
                break
                
    def process_data(self, data):
        try:
            parts = data.split(',')
            if len(parts) >= 5:
                timestamp, symbol, price, volume, change = parts
                stock_data = {
                    'timestamp': timestamp,
                    'symbol': symbol,
                    'price': float(price),
                    'volume': int(volume),
                    'change': float(change)
                }
                self.data_buffer.append(stock_data)
                self.display_stock_data(stock_data)
        except:
            pass
            
    def display_stock_data(self, data):
        arrow = "▲" if data['change'] >= 0 else "▼"
        print(f"{data['timestamp']} | {data['symbol']} | "
              f" | Vol: {data['volume']:,} | "
              f"{arrow} {abs(data['change']):.2f}%")
              
    def save_to_csv(self, filename="stock_data.csv"):
        if self.data_buffer:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['timestamp', 'symbol', 'price', 'volume', 'change']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for data in self.data_buffer:
                    writer.writerow(data)
            print(f"Data saved to {filename}")
            
    def disconnect(self):
        self.running = False
        if self.socket:
            self.socket.close()
        print("Disconnected from server")

if __name__ == "__main__":
    client = StockDataClient()
    if client.connect():
        try:
            time.sleep(30)
            client.save_to_csv()
        finally:
            client.disconnect()
