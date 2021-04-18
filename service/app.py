from flask import Flask

app = Flask(__name__)


@app.route('/api/users', methods=['GET'])
def something():
    return 'something'

if __name__ == '__main__':
    app.run(debug=True)
