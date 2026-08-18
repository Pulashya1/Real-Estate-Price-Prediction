# Bengaluru House Price Prediction

A lightweight web app that predicts house prices (in Lakhs) for Bengaluru based on area, BHK, bathrooms, and location. The frontend is a simple static UI in the `client/` folder and the backend is a Flask app in `server/` that loads a pre-trained model from `server/artifacts/`.


**Key Features**
- Simple, responsive single-page UI for quick price estimates.
- Flask API endpoints: `/api/get_location_names` and `/api/predict_home_price`.
- Pretrained model and columns stored in `server/artifacts/`.

- ![Uploading image.png…]()


**Quick Start (Development)**

- Requirements: Python 3.8+, pip

1. Install dependencies

```bash
pip install flask numpy scikit-learn
```

2. Run the server from the project root

```bash
python server/server.py
```

3. Open the app in a browser

- Go to: http://127.0.0.1:5000/

**API Usage**

- Get locations:
  - `GET /api/get_location_names`
- Predict price (form or JSON):
  - `POST /api/predict_home_price` with fields: `total_sqft`, `bhk`, `bath`, `location`

Example curl:

```bash
curl -X POST http://127.0.0.1:5000/api/predict_home_price \
  -d total_sqft=1000 -d bhk=2 -d bath=2 -d location="1st phase jp nagar"
```


**Troubleshooting**
- If the server fails to start, ensure `server/artifacts/columns.json` and `banglore_home_prices_model.pickle` exist.
- If an endpoint returns `invalid input`, confirm the POST body includes all required fields.

