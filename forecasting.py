import numpy as np
from data_loader import load_sales_data

def revenue_forecast():

    sales = load_sales_data()

    avg_sales = np.mean(sales['Sales'])

    forecast = avg_sales * 1.10

    return round(forecast, 2)