export interface Order {
  price: number,
  size: number,
}
export interface ServerRespond {
  stock: string,
  top_bid: Order,
  top_ask: Order,
  timestamp: Date,
}

class DataStreamer {
  static API_URL: string = 'http://localhost:8080/query?id=1';

  static getData(callback: (data: ServerRespond[]) => void): void {
