# Investment Advisor Chatbot

This Investment Advisor Chatbot is a Streamlit web app that leverages financial data from Yahoo Finance to provide insights into market trends and offer personalized investment advice based on risk tolerance. It utilizes **yfinance** for stock data, **matplotlib** and **plotly** for data visualization, and **Streamlit** for an interactive user experience.

## Features

- **Market Trend Analysis**: Fetches data for major indices like the S&P 500 and visualizes market trends over the last 30 days.
- **Investment Advice**: Provides general investment advice based on recent market trends.
- **Risk Assessment**: Assesses the user’s risk tolerance and suggests investment types tailored to different risk levels (Low, Medium, High).

## Tech Stack

- **Python**: Programming language for backend processing.
- **yfinance**: Fetches real-time stock data.
- **Streamlit**: Creates an interactive web app.
- **Matplotlib & Plotly**: Visualize stock data with static and interactive charts.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MonalisaThomas/financial-advisor-chat.git
    cd your-repository-name
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run investment_app.py
    ```

## How to Use

1. **Market Query**: Type a question such as "How is the market today?" to get an update on the S&P 500’s recent performance, along with a visual representation of its closing price trend.
2. **Investment Advice**: Ask for investment advice (e.g., "What should I invest in?") to receive guidance based on recent market performance.
3. **Risk Assessment**: Select your risk level from Low, Medium, or High, and the chatbot will recommend investment types that suit your tolerance.

## Code Overview

- `get_stock_data(ticker, period="1mo")`: Fetches historical stock data for a specified ticker.
- `plot_market_trends_matplotlib(data, ticker)`: Displays a static line chart of the stock’s closing price over time using Matplotlib.
- `plot_market_trends_plotly(data, ticker)`: Displays an interactive line chart of the stock’s closing price using Plotly.
- `get_investment_advice()`: Provides general advice based on S&P 500 performance.
- `risk_assessment(risk_level)`: Suggests investment types based on user’s risk tolerance.

## Example Queries

- "How is the market today?"
- "What should I invest in?"
- "Suggest investments for a low-risk profile."

## Dependencies

- `yfinance`
- `streamlit`
- `matplotlib`
- `plotly`
- `pandas`

Add these dependencies in `requirements.txt` to ensure the project runs smoothly.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

Feel free to reach out or contribute to the project. Your suggestions and feedback are welcome!

---

Happy investing!
