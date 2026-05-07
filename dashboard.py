from sales_analysis import total_sales
from forecasting import revenue_forecast

def generate_dashboard():

    dashboard_data = {
        "total_sales": total_sales(),
        "forecast": revenue_forecast()
    }

    return dashboard_data