from flask import Flask, request, jsonify
import util
import os

# Serve client static files from ../client
client_folder = os.path.join(os.path.dirname(__file__), '..', 'client')
app = Flask(__name__, static_folder=client_folder, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('app.html')


@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    # Accept form-encoded or JSON payloads
    data = request.form if request.form else request.get_json(force=True, silent=True)
    try:
        total_sqft = float(data.get('total_sqft'))
        location = data.get('location')
        bhk = int(data.get('bhk'))
        bath = int(data.get('bath'))
    except Exception:
        return jsonify({'error': 'invalid input'}), 400

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True, host='0.0.0.0', port=5000)