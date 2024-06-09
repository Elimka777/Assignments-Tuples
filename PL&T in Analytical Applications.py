def average_closing_price(stock_data, stock_symbol):
    total_price = 0
    count = 0
    for symbol, date, price in stock_data:
        if symbol == stock_symbol:
            total_price += price
            count += 1
    if count == 0:
        return f"No data available for stock symbol: {stock_symbol}"
    else:
        average_price = total_price / count
        return f"The average closing price for {stock_symbol} is {average_price:.2f}"

# Sample Data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-03", 135.0),
    ("MSFT", "2021-01-02", 225.0),
]

# Example usage
print(average_closing_price(stock_data, "AAPL"))
print(average_closing_price(stock_data, "MSFT"))
print(average_closing_price(stock_data, "GOOGL"))