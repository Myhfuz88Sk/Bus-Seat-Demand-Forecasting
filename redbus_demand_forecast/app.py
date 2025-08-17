# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# import pickle
# import datetime

# app = Flask(__name__)

# with open('trained_model.pkl', 'rb') as f:
#     model = pickle.load(f)

# @app.route('/')
# def index():
#     return render_template('index.html')
#     # return render_template('state.html')

# @app.route('/state')
# def state():
#     return render_template('state.html')

# @app.route('/forecast', methods=['POST'])
# def forecast():
#     data = request.get_json()
#     try:
#         doj = pd.to_datetime(data['doj'])
#         srcid = int(data['srcid'])
#         destid = int(data['destid'])

#         features = pd.DataFrame([{
#             'srcid': srcid,
#             'destid': destid,
#             'day_of_week': doj.weekday(),
#             'day_of_month': doj.day,
#             'month': doj.month,
#             'year': doj.year,
#             'week_of_year': doj.isocalendar().week,
#             'is_weekend': int(doj.weekday() >= 5)
#         }])

#         # Predict
#         predicted_demand = model.predict(features)[0]
#         return jsonify({'success': True, 'demand': int(predicted_demand)})
#     except Exception as e:
#         print("Forecast error:", e)
#         return jsonify({'success': False})

# if __name__ == '__main__':
#     app.run(debug=True)




















from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import datetime

app = Flask(__name__)

# Load the trained model
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Route for the main page (Andhra Pradesh & Telangana Districts)

@app.route('/')
def india():
    return render_template('state.html')


# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# # Route for the Bus Demand Forecast page
# @app.route('/state.html')
# def state():
#     return render_template('state.html')

# Route to handle the forecast prediction
@app.route('/forecast', methods=['POST'])
def forecast():
    data = request.get_json()
    try:
        doj = pd.to_datetime(data['doj'])
        srcid = int(data['srcid'])
        destid = int(data['destid'])

        features = pd.DataFrame([{
            'srcid': srcid,
            'destid': destid,
            'day_of_week': doj.weekday(),
            'day_of_month': doj.day,
            'month': doj.month,
            'year': doj.year,
            'week_of_year': doj.isocalendar().week,
            'is_weekend': int(doj.weekday() >= 5)
        }])

        # Predict the demand
        predicted_demand = model.predict(features)[0]
        return jsonify({'success': True, 'demand': int(predicted_demand)})
    except Exception as e:
        print("Forecast error:", e)
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)
