from data_loader import load_sales_data

def total_sales():

    sales = load_sales_data()

    return sales['Sales'].sum()

def top_products():

    sales = load_sales_data()

    top = sales.groupby('Product')['Sales'].sum()

    return top.sort_values(ascending=False).head(5)