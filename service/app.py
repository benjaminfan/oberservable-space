from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
import mock_db

app = Flask(__name__)
app.config.from_object('config.Mock')
app.url_map.strict_slashes = False

# Mongo middleware not implemented
db = (mock_db.MockCRUD(), MongoEngine())[app.config.get('USE_MONGO')]


@app.route('/api/agents/', methods=['GET', 'POST'])
def handle_agents():
    if request.method == 'GET':
        return jsonify(db.agents)

    if request.method == 'POST':
        params = request.json
        try:
            db.add_agent(params)
            return jsonify({"result": "Created new agent {}".format(params.get('_id'))})
        except AttributeError as e:
            return jsonify({"error": "{}".format(e)}), 400


@app.route('/api/agent/<int:id>', methods=['GET', 'PUT'])
def handle_agent_by_id(id):
    if request.method == 'GET':
        agent_data = db.agents.get(id, False)
        if agent_data is False:
            return jsonify("Agent {} not found".format(id)), 400
        return jsonify(agent_data)

    if request.method == 'PUT':
        params = request.json
        try:
            db.update_agent(id, params)
            return jsonify({"result": "Updated agent {}".format(id)})
        except AttributeError as e:
            return jsonify({"error": "{}".format(e)}), 400


@app.route('/api/agent/<int:id>/customers/', methods=['GET'])
def view_agent_customer_data(id):
    try:
        return jsonify(db.get_customers_per_agent(id))
    except KeyError as e:
        return jsonify({"error": "Agent {} not found. ".format(e)}), 400


@app.route('/api/customer/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_customer_by_id(id):
    if request.method == 'GET':
        customer_data = db.customers.get(id, False)
        if customer_data is False:
            return jsonify("Customer {} not found".format(id)), 400
        return jsonify(customer_data)

    if request.method == 'PUT':
        params = request.json
        try:
            db.update_customer(id, params)
            return jsonify({"result": "Updated Customer {}".format(id)})
        except AttributeError as e:
            return jsonify({"error": "{}".format(e)}), 400

    if request.method == 'DELETE':
        try:
            del db.customers[id]
            return jsonify({"result": "Deleted Customer {}".format(id)})
        except KeyError as e:
            return jsonify({"error": "Customer not found {}".format(e)}), 400


@app.route('/api/customers/', methods=['GET'])
def view_customers():
    return jsonify(db.customers)


@app.errorhandler(404)
def handle_404(e):
    return jsonify('Invalid Route Requested. Please check your trailing slash')


@app.errorhandler(500)
def catch_server_errors(e):
    return jsonify('Unhandled Exception Has Occurred')


if __name__ == '__main__':
    app.run(debug=True)
