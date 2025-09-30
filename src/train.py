import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def load_data(path):
    df = pd.read_csv(path)
    return df

def train_model(data_path, out_path):
    df = load_data(data_path)
    
    X = df.drop("price", axis=1)
    y = df["price"]

    # kategorik ustunni one-hot qilish
    X = pd.get_dummies(X, columns=["location"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Test R^2 score: {score:.2f}")

    joblib.dump(model, out_path)
    print(f"Model saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--out", type=str, required=True)
    args = parser.parse_args()

    train_model(args.data, args.out)
