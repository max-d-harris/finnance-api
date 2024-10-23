from typing import Union

from fastapi import FastAPI

from database import connect, get_stocks, get_companies, get_stock_price_by_ticker

app = FastAPI()

@app.get("/")
def home_page():
    return {"Hello, welcome to the FinanceAPI! - see http://127.0.0.1:8000/docs for the docs!"}

@app.get("/companies")
def companies_page():
    companies = get_companies()

    
    if not companies:
        return {"message": "No company data available"}

    return companies

@app.get("/stocks")
def stocks_page():

    stocks = get_stocks()

    if not stocks:
        return {"message": "No stock data available"}

    return stocks

@app.get("/stocks/{ticker}")
def price_page(ticker: str):
    stock_price = get_stock_price_by_ticker(ticker)

    if stock_price is None:
        return {"message": "No stock found for ticker: {}".format(ticker)}

    return stock_price

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)