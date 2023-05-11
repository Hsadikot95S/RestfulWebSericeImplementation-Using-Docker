import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Load Json file
def load_data():
    with open('customers.json', 'r') as f:
        data = json.load(f)
    return data

# Route to display the root page which is the welcome page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Route to display all customers

@app.route('/customers', methods=['GET'])
def customers():
    data = load_data()
    return render_template('customers.html', customers=data['customers'])

# Route to display a single customer by ID

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    data = load_data()
    customers = data['customers']
    customer = next((c for c in customers if int(c["userId"]) == id), None)

    if customer:
        return render_template('single_customer.html', customer=customer)
    else:
        return jsonify({"message": f"Customer with ID {id} not found"}), 404

# Route to display all orders for a given customer ID
@app.route('/customers/<int:id>/orders', methods=['GET'])
def get_orders_by_customer(id):
    data = load_data()
    customers = data['customers']
    customer = next((c for c in customers if int(c["userId"]) == id), None)

    if customer:
        orders = customer.get("orders", [])
        return render_template('customer_orders.html', customer_id=id, customers=[customer], orders=orders)
    else:
        return jsonify({"message": f"Customer with ID {id} not found"}), 404


# Route to display a single order by customer and order ID

@app.route('/customers/<int:customer_id>/orders/<int:order_id>', methods=['GET'])
def get_order(customer_id, order_id):
    data = load_data()
    customers = data['customers']
    customer = next((c for c in customers if int(c["userId"]) == customer_id), None)

    if customer:
        orders = customer.get("orders", [])
        order = next((o for o in orders if int(o["orderId"]) == order_id), None)

        if order:
            return render_template('single_order.html', customer_id=customer_id, order=order,lineItems=order['lineItems'])
        else:
            return jsonify({"message": f"Order with ID {order_id} for customer {customer_id} not found"}), 404
    else:
        return jsonify({"message": f"Customer with ID {customer_id} not found"}), 404

# Start the Flask App.
if __name__ == '__main__':
    app.run(debug=True)
