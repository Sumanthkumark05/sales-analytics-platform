from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    data = {
        "total_sales": 25000,
        "forecast": 30000
    }

    return render_template(
        'dashboard.html',
        data=data
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)