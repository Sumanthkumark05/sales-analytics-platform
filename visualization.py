import matplotlib.pyplot as plt
from sales_analysis import top_products

def sales_chart():

    data = top_products()

    data.plot(kind='bar')

    plt.title('Top Products')

    plt.xlabel('Products')

    plt.ylabel('Sales')

    plt.savefig('static/sales_chart.png')