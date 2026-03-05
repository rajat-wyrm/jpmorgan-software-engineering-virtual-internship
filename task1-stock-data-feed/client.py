def getDataPoint(quote):
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])

    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    if price_b == 0:
        return None
    return price_a / price_b
