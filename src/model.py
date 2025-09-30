# src/model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from joblib import dump, load


def get_pipeline():
pipeline = Pipeline([
('scaler', StandardScaler()),
('rf', RandomForestRegressor(n_estimators=100, random_state=42))
])
return pipeline




def save_model(model, path: str):
dump(model, path)




def load_model(path: str):
return load(path)