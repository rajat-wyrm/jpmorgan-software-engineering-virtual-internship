interface StockDataPoint {
    timestamp: Date;
    symbol: string;
    price: number;
    volume: number;
    change: number;
}

class TradingDashboard {
    private symbols: string[];
    private data: Map<string, StockDataPoint[]>;
    private ws: WebSocket | null;
    
    constructor(symbols: string[] = ['JPM', 'GS', 'MS', 'BAC', 'C']) {
        this.symbols = symbols;
        this.data = new Map();
        this.ws = null;
        symbols.forEach(symbol => this.data.set(symbol, []));
    }
    
    public connect(): void {
        this.ws = new WebSocket('ws://localhost:8080');
        
        this.ws.onopen = () => {
            console.log('Connected to server');
            this.ws?.send(JSON.stringify({
                type: 'subscribe',
                symbols: this.symbols
            }));
        };
        
        this.ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            if (message.type === 'data') {
                this.processData(message.data);
            }
        };
        
        this.ws.onclose = () => {
            console.log('Disconnected, reconnecting in 5s...');
            setTimeout(() => this.connect(), 5000);
        };
    }
    
    private processData(dataPoints: StockDataPoint[]): void {
        dataPoints.forEach(point => {
            const symbolData = this.data.get(point.symbol) || [];
            symbolData.push({
                ...point,
                timestamp: new Date(point.timestamp)
            });
            
            if (symbolData.length > 100) {
                symbolData.shift();
            }
            
            this.data.set(point.symbol, symbolData);
        });
        
        this.updateDisplay();
    }
    
    private updateDisplay(): void {
        const container = document.getElementById('dashboard');
        if (!container) return;
        
        let html = '<div class="dashboard-grid">';
        
        this.symbols.forEach(symbol => {
            const data = this.data.get(symbol) || [];
            const latest = data[data.length - 1];
            
            if (latest) {
                const changeClass = latest.change >= 0 ? 'positive' : 'negative';
                html += 
                    <div class="stock-card">
                        <h3></h3>
                        <div class="price">UTF8{latest.price.toFixed(2)}</div>
                        <div class=""> %</div>
                        <div class="volume">Vol: </div>
                    </div>
                ;
            }
        });
        
        html += '</div>';
        container.innerHTML = html;
    }
    
    public disconnect(): void {
        if (this.ws) {
            this.ws.close();
        }
    }
}

// Initialize dashboard
document.addEventListener('DOMContentLoaded', () => {
    const dashboard = new TradingDashboard();
    dashboard.connect();
    
    window.addEventListener('beforeunload', () => {
        dashboard.disconnect();
    });
});
