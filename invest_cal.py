def inputs(from_stock_rate):
    r = from_stock_rate
    print(from_stock_rate)
    p = int(input("How much would you like to invest?"))
    t = int(input("How long would you like to invest in years?"))
    n = int (1)
    r_float = r/100
    a = int((p)*((1+(r_float/n))**(n*t)))
    print(f"Your investment will grow to {a} after {t} years")
    
def stock_rate():
    previous = float(input("What was the stock price?"))
    current = float(input("What is the current stock price?"))
    invest_rate = int(100*((current-previous)/previous))
    return invest_rate

def calculator():
    stockrate = stock_rate()
    print(stockrate)
    inputs(stockrate)
    
#this is a new comment  
calculator()
