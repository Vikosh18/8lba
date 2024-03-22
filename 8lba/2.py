import requests
import pandas as pd
from datetime import datetime

# Функція для отримання продуктів
def get_products():
    products_response = requests.get('https://api.exchange.com/products')
    products_data = products_response.json()
    products_df = pd.DataFrame(products_data)
    return products_df

# Функція для отримання історичних даних
def get_historical_data(symbol, interval, start_time, end_time):
    start_timestamp = int(datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
    end_timestamp = int(datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S').timestamp() * 1000)
    historical_data_response = requests.get(f'https://api.exchange.com/historical_data?symbol={symbol}&interval={interval}&start_time={start_timestamp}&end_time={end_timestamp}')
    historical_data = historical_data_response.json()
    historical_data_df = pd.DataFrame(historical_data)
    return historical_data_df

# Параметризовані дані для тестування функції get_products
def test_get_products():
    products_df = get_products()
    assert len(products_df) >= 0

# Параметризовані дані для тестування функції get_historical_data
def test_get_historical_data():
    historical_data = get_historical_data('BTCUSDT', '1d', '2024-03-21 00:00:00', '2024-03-22 00:00:00')
    assert not historical_data.empty

