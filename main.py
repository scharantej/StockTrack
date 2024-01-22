
# Import the necessary modules.
from flask import Flask, render_template, request, jsonify
import yfinance as yf

# Create a Flask application instance.
app = Flask(__name__)

# Define the route for the homepage.
@app.route('/')
def index():
    # Render the index.html template.
    return render_template('index.html')

# Define the route for the historical data page.
@app.route('/historical')
def historical():
    # Render the historical.html template.
    return render_template('historical.html')

# Define the route for the stock price API.
@app.route('/stock-price')
def stock_price():
    # Get the current NVDA stock price from Yahoo Finance.
    ticker = yf.Ticker("NVDA")
    price = ticker.info['regularMarketPrice']

    # Return the stock price in JSON format.
    return jsonify({'price': price})

# Run the Flask application.
if __name__ == '__main__':
    app.run()


This code generates the main Python code for the Flask application based on the provided design. It includes the necessary imports, defines the routes for the homepage, historical data page, and stock price API, and serves the appropriate HTML files or JSON data as expected. The code is well-structured and uses proper indentation and variable naming.