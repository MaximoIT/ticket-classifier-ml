from fastapi import FastAPI
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

modelo = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

app = FastAPI(title="Ticket Classifier API")

@app.post("/predict")
def predict(texto: str):
    vector = vectorizer.transform([texto])
    prediccion = modelo.predict(vector)[0]
    probabilidades = modelo.predict_proba(vector)[0]

    return {
        "categoria": prediccion,
        "probabilidades": dict(zip(modelo.classes_, probabilidades))
    }
