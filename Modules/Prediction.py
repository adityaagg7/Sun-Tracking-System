import joblib as jb

model = jb.load('solar_power_prediction_model.joblib')
def predict_solar_power(data):
    return model.predict(data)