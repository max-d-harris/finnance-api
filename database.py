import mysql.connector

def connect():
    database_connection = mysql.connector.connect(
        host="localhost",
        user="financeapi",
        password="password",
        database="finance_db"
    )

    cursor = database_connection.cursor()

    return database_connection, cursor

import mysql.connector

def connect():
    database_connection = mysql.connector.connect(
        host="localhost",
        user="financeapi",
        password="password",
        database="finance_db"
    )
    cursor = database_connection.cursor()
    return database_connection, cursor

def get_stocks():
    database_connection, cursor = connect()

    query = "SELECT company_name, stock_ticker, price, market FROM stocks"
    cursor.execute(query)
    
    stocks = cursor.fetchall()

    cursor.close()
    database_connection.close()

    stock_list = [
        {
            "company_name": stock[0],
            "stock_ticker": stock[1],
            "price": stock[2],
            "market": stock[3]
        }
        for stock in stocks
    ]

    return stock_list

def get_companies():
    
    database_connection, cursor = connect()

    query = "SELECT company_name from stocks"
    cursor.execute(query)

    companies = cursor.fetchall()

    cursor.close()
    database_connection.close()

    return companies

def get_stock_price_by_ticker(ticker: str):
    database_connection, cursor = connect()

    query = "SELECT stock_ticker, price FROM stocks WHERE stock_ticker = %s"

    try:
        
        cursor.execute(query, (ticker,))
        result = cursor.fetchone()

        if result:
            return {
                "stock_ticker": result[0],
                "price": result[1]
            }
        else:
            return {"message": "Stock information not found for {}".format(ticker)}
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return {"message": "Database error occurred"}

    finally:
        cursor.close()
        database_connection.close()

def main():
    database_connection, cursor = connect()

    stocks = get_stocks(cursor)

    for stock in stocks:
        print(stock)

    cursor.close()

    database_connection.close()

if __name__ == "__main__":
    main()