# Bus-Seat-Demand-Forecasting(ML)
Developed a machine learning model to forecast seat demand on bus routes up to 15 days in advance, using features like route, date, seasonality, and travel patterns.
This project predicts seat demand on bus routes for a given journey date, source, and destination using machine learning.
It includes a Flask backend API for predictions and an interactive frontend that displays results in real-time.

🚀 Features

Forecasts seat demand up to 15 days in advance.

Feature engineering on date and route attributes (day of week, month, weekend, etc.).

Flask API endpoint (/forecast) for real-time predictions.

Frontend integration with spinner, styled success/error messages, and demand visualization.

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Machine Learning: scikit-learn / TensorFlow (trained model)

Data Processing: pandas, numpy

⚡ Usage
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Flask app
python app.py

3️⃣ Open in browser

Go to: http://127.0.0.1:5000

🔮 Example API Call

POST /forecast

{
  "doj": "2025-08-20",
  "srcid": "101",
  "destid": "205"
}


Response

{
  "success": true,
  "demand": 128
}

git clone https://github.com/Myhfuz88Sk/Bus-Seat-Demand-Forecasting.git
cd bus-seat-forecast

📊 Model Training (Summary)

Collected booking/search history data.

Extracted temporal features (weekday, weekend, month, seasonality).

Trained regression model to predict seat demand (evaluated using RMSE).

📌 Future Improvements

Incorporate holiday and festival data to improve demand accuracy.

Add visual demand trend charts to frontend.

Deploy on AWS / Heroku for public access.
