import express from 'express';
import WebSocket from 'ws';
import http from 'http';

interface StockData {
    timestamp: string;
    symbol: string;
    price: number;
    volume: number;
    change: number;
}

class PerspectiveServer {
    private app: express.Application;
    private server: http.Server;
    private wss: WebSocket.Server;
    private symbols: string[] = ['JPM', 'GS', 'MS', 'BAC', 'C'];
    
    constructor(port: number = 8080) {
        this.app = express();
        this.server = http.createServer(this.app);
        this.wss = new WebSocket.Server({ server: this.server });
        this.setupMiddleware();
        this.setupWebSocket();
    }
    
    private setupMiddleware(): void {
        this.app.use(express.static('public'));
        this.app.get('/api/historical/:symbol', (req, res) => {
            res.json(this.generateHistoricalData(req.params.symbol));
        });
    }
    
    private setupWebSocket(): void {
        this.wss.on('connection', (ws: WebSocket) => {
            console.log('Client connected');
            
            ws.on('message', (message: string) => {
                try {
                    const data = JSON.parse(message);
                    if (data.type === 'subscribe') {
                        console.log(Subscribed to: );
                    }
                } catch (error) {
                    console.error('Error:', error);
                }
            });
        });
    }
    
    private generateStockData(): StockData {
        return {
            timestamp: new Date().toISOString(),
            symbol: this.symbols[Math.floor(Math.random() * this.symbols.length)],
            price: 100 + Math.random() * 100,
            volume: Math.floor(1000 + Math.random() * 9000),
            change: (Math.random() - 0.5) * 10
        };
    }
    
    private generateHistoricalData(symbol: string): StockData[] {
        const data: StockData[] = [];
        const now = Date.now();
        
        for (let i = 0; i < 100; i++) {
            data.push({
                timestamp: new Date(now - i * 60000).toISOString(),
                symbol,
                price: 100 + Math.random() * 100,
                volume: Math.floor(1000 + Math.random() * 9000),
                change: (Math.random() - 0.5) * 10
            });
        }
        return data;
    }
    
    private startDataStreaming(): void {
        setInterval(() => {
            const data = this.generateStockData();
            const message = JSON.stringify({
                type: 'data',
                data: [data]
            });
            
            this.wss.clients.forEach((client) => {
                if (client.readyState === WebSocket.OPEN) {
                    client.send(message);
                }
            });
        }, 1000);
    }
    
    public start(): void {
        const PORT = process.env.PORT || 8080;
        this.server.listen(PORT, () => {
            console.log(Server running on http://localhost:);
            this.startDataStreaming();
        });
    }
}

const server = new PerspectiveServer();
server.start();
