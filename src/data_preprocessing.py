# src/data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(path: str):
df = pd.read_csv(path)
return df




def preprocess(df: pd.DataFrame):
# oddiy misol: kerakli ustunlarni tanlash va tozalash
df = df.copy()
# misol ustunlar: rooms, area, location, year_built, metro_distance, price
df = df.dropna(subset=['price', 'area'])


# location ni kategoriqga aylantirish (one-hot yoki target encoding)
df = pd.get_dummies(df, columns=['location'], drop_first=True)


X = df.drop(columns=['price'])
y = df['price']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
return X_train, X_test, y_train, y_test