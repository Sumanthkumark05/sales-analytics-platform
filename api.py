from flask import Blueprint, jsonify
from sales_analysis import total_sales

api = Blueprint('api', __name__)

@api.route('/sales')
def sales_api():

    return jsonify({
        "total_sales": total_sales()
    })