import unittest
import threading
import time
from client3 import StockDataClient

class TestStockDataClient(unittest.TestCase):
    
    def test_client_initialization(self):
        client = StockDataClient('localhost', 9999)
        self.assertEqual(client.host, 'localhost')
        self.assertEqual(client.port, 9999)
        
    def test_connection_failure(self):
        client = StockDataClient('localhost', 9998)
        result = client.connect()
        self.assertFalse(result)
        
    def test_data_buffer(self):
        client = StockDataClient('localhost', 9999)
        self.assertEqual(len(client.data), 0)

if __name__ == '__main__':
    unittest.main()
