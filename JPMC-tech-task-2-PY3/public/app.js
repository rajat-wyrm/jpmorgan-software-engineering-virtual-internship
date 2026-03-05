class PerspectiveDashboard {
    constructor() {
        this.viewer = document.getElementById('view1');
        this.connectionStatus = document.getElementById('connection-status');
        this.dataCount = document.getElementById('data-count');
        this.lastUpdate = document.getElementById('last-update');
        this.ws = null;
        this.data = [];
        
        this.initViewer();
        this.setupEventListeners();
    }
    
    async initViewer() {
        await this.viewer.restore({
            columns: ['timestamp', 'symbol', 'price', 'volume', 'change'],
            'aggregates': {
                'timestamp': 'distinct count',
                'symbol': 'distinct count',
                'price': 'avg',
                'volume': 'sum',
                'change': 'avg'
            }
        });
    }
    
    setupEventListeners() {
        document.getElementById('connect-btn').addEventListener('click', () => this.connect());
        document.getElementById('disconnect-btn').addEventListener('click', () => this.disconnect());
        document.getElementById('symbol-select').addEventListener('change', (e) => this.filterSymbol(e.target.value));
    }
    
    connect() {
        this.ws = new WebSocket('ws://localhost:8080');
        
        this.ws.onopen = () => {
            this.connectionStatus.textContent = 'Connected';
            this.connectionStatus.classList.add('connected');
            this.ws.send(JSON.stringify({
                type: 'subscribe',
                symbols: ['JPM', 'GS', 'MS', 'BAC', 'C']
            }));
        };
        
        this.ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            if (message.type === 'data') {
                this.updateData(message.data);
            }
        };
        
        this.ws.onclose = () => {
            this.connectionStatus.textContent = 'Disconnected';
            this.connectionStatus.classList.remove('connected');
        };
        
        this.ws.onerror = (error) => {
            console.error('WebSocket error:', error);
            alert('Connection error. Make sure the server is running.');
        };
    }
    
    disconnect() {
        if (this.ws) {
            this.ws.close();
        }
    }
    
    async updateData(newData) {
        this.data = [...this.data, ...newData];
        if (this.data.length > 1000) {
            this.data = this.data.slice(-1000);
        }
        
        await this.viewer.update(this.data);
        
        this.dataCount.textContent = this.data.length;
        if (newData.length > 0) {
            this.lastUpdate.textContent = new Date().toLocaleTimeString();
        }
    }
    
    async filterSymbol(symbol) {
        if (symbol === 'all') {
            await this.viewer.restore({ filter: [] });
        } else {
            await this.viewer.restore({ filter: [['symbol', '==', symbol]] });
        }
    }
}

// Initialize dashboard
document.addEventListener('DOMContentLoaded', () => {
    new PerspectiveDashboard();
});
