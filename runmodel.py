import joblib
model = joblib.load('marks_model.pkl')
model.predict([[8]])
