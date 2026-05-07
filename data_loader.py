import pandas as pd

def load_sales_data():

    sales = pd.read_csv('datasets/sales.csv')

    return sales

def load_customer_data():

    customers = pd.read_csv('datasets/customers.csv')

    return customers