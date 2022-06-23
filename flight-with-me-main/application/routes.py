from __init__ import *
app = Flask(__name__)

@app.route('/flights', methods=['GET'])

# GET specific flight
@app.route('/flight/<id>', methods=['GET'])

# CREATE flight
@app.route('/flight', methods=['POST'])

# DELETE Flight
@app.route('/flight/<id>', methods=['DELETE'])

#UPDATE Flight
@app.route('/flight/<id>', methods=['PUT'])
