import joblib
model = joblib.load('marks_model.pk1')
model.predict([[8]])
