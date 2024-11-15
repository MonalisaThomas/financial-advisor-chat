import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd

# Function to fetch stock data using yfinance
def get_stock_data(ticker, period="1mo"):  # Default period is now 1 month
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    if data.empty:
        return None
    return data

# Function to plot market trends using matplotlib
def plot_market_trends_matplotlib(data, ticker):
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label=f"{ticker} Closing Price", color="b")
    plt.title(f"{ticker} Market Trend over the Last 30 Days")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=45)
    plt.legend(loc="best")
    plt.grid(True)
    st.pyplot(plt)

# Function to plot market trends using plotly (interactive graph)
def plot_market_trends_plotly(data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{ticker} Closing Price'))
    fig.update_layout(title=f"{ticker} Market Trend over the Last 30 Days",
                      xaxis_title="Date",
                      yaxis_title="Price ($)",
                      template="plotly_dark")
    st.plotly_chart(fig)

# Function to analyze market trends
def get_market_trends():
    # Example of fetching some major indices data (S&P 500)
    sp500 = get_stock_data('^GSPC')  # S&P 500 index
    return sp500

# Function to provide investment advice based on market trends
def get_investment_advice():
    sp500 = get_stock_data('^GSPC', period="1d")  # Last day's data
    if not sp500.empty:
        if sp500['Close'][0] > 4000:  # If S&P 500 is higher, assume bullish market
            return "Consider investing in stocks or ETFs that are showing upward trends."
        else:
            return "It might be a good time to consider bonds or safe-haven assets."
    return "No market data available for today."

# Function to assess user’s risk tolerance and suggest investment types
def risk_assessment(risk_level):
    if risk_level.lower() == "low":
        return "Consider investing in bonds, index funds, or other stable investments."
    elif risk_level.lower() == "medium":
        return "A balanced portfolio of stocks and bonds would be suitable."
    elif risk_level.lower() == "high":
        return "Consider aggressive investments such as tech stocks, cryptocurrencies, or high-risk ETFs."
    else:
        return "Please specify a valid risk level (low, medium, high)."

# Streamlit app function for user interaction
def main():
    st.title("Investment Advisor Chatbot")
    
    # Input text from the user
    query = st.text_input("Ask the chatbot (e.g., 'How is the market today?')")

    # Process the query
    if query:
        if "market" in query.lower():
            sp500_data = get_market_trends()  # Get market trend data (S&P 500)
            if sp500_data is not None and not sp500_data.empty:
                response = f"Market Update: Today's S&P 500 closing price is {sp500_data['Close'][0]:.2f}"
                st.write(response)

                # Show a graph of the market trends
                st.subheader("Market Trend Visualization")
                plot_market_trends_plotly(sp500_data, "^GSPC")
            else:
                st.write("No data available for the S&P 500 index at the moment.")
            
        elif "invest" in query.lower():
            response = get_investment_advice()
            st.write(f"Investment Advice: {response}")
        else:
            st.write("I'm sorry, I didn't understand that. Please ask about the market or investment advice.")
    
    # Risk Assessment Form
    st.subheader("Risk Assessment")
    risk_level = st.selectbox("Select your risk level", ["Low", "Medium", "High"])
    if st.button("Get Investment Advice based on Risk Level"):
        advice = risk_assessment(risk_level)
        st.write(f"Based on your risk level, {advice}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
