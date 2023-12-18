import joblib as jb
import os
from TestProj.settings import BASE_DIR

model_path = os.path.join(BASE_DIR, 'APP', 'Modules', 'solar_power_prediction_model.joblib')
model = jb.load(model_path)

m = {'Sunny': 'Sunny',
     'Partly cloudy': 'Partly Sunny',
     'Cloudy': 'Cloudy',
     'Overcast': 'Cloudy',
     'Mist': 'Fog',
     'Patchy rain possible': 'Passing Clouds',
     'Patchy snow possible': 'Passing Clouds',
     'Patchy sleet possible': 'Passing Clouds',
     'Patchy freezing drizzle possible': 'Passing Clouds',
     'Thundery outbreaks possible': 'Scattered Clouds',
     'Blowing snow': 'Scattered Clouds',
     'Blizzard': 'Scattered Clouds',
     'Fog': 'Fog',
     'Freezing fog': 'Scattered Clouds',
     'Patchy light drizzle': 'Passing Clouds',
     'Light drizzle': 'Scattered Clouds',
     'Freezing drizzle': 'Scattered Clouds',
     'Heavy freezing drizzle': 'Scattered Clouds',
     'Patchy light rain': 'Passing Clouds',
     'Light rain': 'Scattered Clouds',
     'Moderate rain at times': 'Scattered Clouds',
     'Moderate rain': 'Scattered Clouds',
     'Heavy rain at times': 'Scattered Clouds',
     'Heavy rain': 'Scattered Clouds',
     'Light freezing rain': 'Scattered Clouds',
     'Moderate or heavy freezing rain': 'Scattered Clouds',
     'Light sleet': 'Scattered Clouds',
     'Moderate or heavy sleet': 'Scattered Clouds',
     'Patchy light snow': 'Passing Clouds',
     'Light snow': 'Scattered Clouds',
     'Patchy moderate snow': 'Passing Clouds',
     'Moderate snow': 'Scattered Clouds',
     'Patchy heavy snow': 'Passing Clouds',
     'Heavy snow': 'Scattered Clouds',
     'Ice pellets': 'Scattered Clouds',
     'Light rain shower': 'Scattered Clouds',
     'Moderate or heavy rain shower': 'Scattered Clouds',
     'Torrential rain shower': 'Scattered Clouds',
     'Light sleet showers': 'Scattered Clouds',
     'Moderate or heavy sleet showers': 'Scattered Clouds',
     'Light snow showers': 'Scattered Clouds',
     'Moderate or heavy snow showers': 'Scattered Clouds',
     'Light showers of ice pellets': 'Scattered Clouds',
     'Moderate or heavy showers of ice pellets': 'Scattered Clouds',
     'Patchy light rain with thunder': 'Passing Clouds',
     'Moderate or heavy rain with thunder': 'Scattered Clouds',
     'Patchy light snow with thunder': 'Passing Clouds',
     'Moderate or heavy snow with thunder': 'Scattered Clouds'
     }


from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder 
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import MinMaxScaler 

num_attr=['temp', 'wind', 'humidity']
cat_attr=['weather']
num_pipeline = Pipeline([ 
    ('imputer', SimpleImputer(strategy='median')), 
    ('scaler', MinMaxScaler()) 
]) 

cat_pipeline = Pipeline([ 
    ('encoder', OneHotEncoder()) 
]) 

full_pipeline = ColumnTransformer([ 
    ('num_pipeline', num_pipeline, num_attr),
    ('cat_pipeline', cat_pipeline, cat_attr) 
]) 

def predict_solar_power(data):
    w = m[data['weather']]
    data['weather']=w
    preped=full_pipeline.fit_transform(data)
    return model.predict(preped)
