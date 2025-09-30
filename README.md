# 🏡 House Price Prediction

Uy narxini bashorat qilish uchun **Machine Learning** loyihasi.
Loyiha **Random Forest Regression** modeliga asoslangan va **FastAPI** yordamida REST API ko‘rinishida taqdim etilgan.

---

## 📂 Loyiha tuzilishi

```
House-Price-Prediction/
│
├── data/               # Dataset fayllari
│   └── raw/house_prices.csv
│
├── models/             # Saqlangan ML modellar
│   └── house_price_rf.joblib
│
├── src/                # Manba kodlari
│   ├── train.py        # Modelni o‘qitish
│   ├── predict.py      # Model yordamida bashorat qilish (script)
│   └── api.py          # FastAPI serveri
│
├── venv/               # Virtual muhit (ignore qilinadi)
│
├── requirements.txt    # Kutubxonalar ro‘yxati
└── README.md           # Hujjat
```

---

## ⚙️ O‘rnatish

1. Repo klon qilish:

   ```bash
   git clone https://github.com/username/House-Price-Prediction.git
   cd House-Price-Prediction
   ```

2. Virtual muhit yaratish:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Kutubxonalarni o‘rnatish:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Modelni o‘qitish

```bash
python src/train.py --data data/raw/house_prices.csv --out models/house_price_rf.joblib
```

---

## 🚀 API ishga tushirish

```bash
uvicorn src.api:app --reload
```

API hozir `http://127.0.0.1:8000` manzilida ishlaydi.
Swagger hujjatlari: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API foydalanish

### 🔹 1. So‘rov yuborish

**Endpoint:**

```
POST /predict
```

**Body (JSON):**

```json
{
  "rooms": 3,
  "area": 80,
  "location": "Tashkent",
  "year_built": 2015,
  "metro_distance": 500
}
```

### 🔹 2. Javob

```json
{
  "predicted_price": 75490
}
```

---

## ✅ Foydalanilgan texnologiyalar

* Python 3.10+
* Pandas, Numpy
* Scikit-learn
* Joblib
* FastAPI
* Uvicorn

---

## 👨‍💻 Muallif

Muslimbek Baratov
<img width="1921" height="2691" alt="screencapture-127-0-0-1-8000-docs-2025-09-30-12_34_51" src="https://github.com/user-attachments/assets/c4b7fdaa-cc70-4c05-b31d-61ccba4d1ded" />
