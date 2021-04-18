from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/agents', methods=['GET, POST'])
def handle_agents():
    params = request.json
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

@app.route('/api/agent/<int:id>', methods=['GET', 'PUT'])
def handle_agent_by_id():
    params = request.json
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass

@app.route('/api/agent/<int:id>/customers', methods=['GET'])
def view_agent_customer_data():
    params = request.json
    if request.method == 'GET':
        pass
    if request.method == 'PUT':
        pass

@app.route('/api/customer/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def handle_customer_by_id():
    return 'something'

@app.route('/api/customers/', methods=['GET'])
def view_customers():
    return 'something'

@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return jsonify('Invalid Route Requested')

if __name__ == '__main__':
    app.run(debug=True)
