export interface Order {
  price: Number,
  size: Number,
}
/**
 * The datafeed server returns an array of ServerRespond with 2 stocks.
 * We do not have to manipulate the ServerRespond for the purpose of this task.
 */
export interface ServerRespond {
  stock: string,
  top_bid: Order,
  top_ask: Order,
  timestamp: Date,
