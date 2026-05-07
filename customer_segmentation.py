from sklearn.cluster import KMeans
from data_loader import load_customer_data

def segment_customers():

    customers = load_customer_data()

    model = KMeans(n_clusters=3)

    customers['Segment'] = model.fit_predict(
        customers[['Age', 'AnnualIncome']]
    )

    return customers