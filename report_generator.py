from sales_analysis import total_sales

def generate_report():

    total = total_sales()

    report = f'''
    Enterprise Sales Report

    Total Sales: {total}
    '''

    with open('reports.txt', 'w') as file:

        file.write(report)

    return report