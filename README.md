# Ticket Classifier (Machine Learning)

Proyecto de Machine Learning para clasificar tickets de soporte en tres categorías:

- bug  
- consulta  
- feature  

El objetivo es automatizar la clasificación inicial de tickets usando técnicas de NLP y exponer el modelo mediante una API.

---

## 📂 Estructura del proyecto

ticket-classifier-ml/
│
├── data/ # Datos de entrenamiento
├── notebooks/ # Exploración y experimentos (Jupyter)
├── src/ # Código productivo
│ ├── api/ # API FastAPI
│ │ └── app.py
│ ├── model/ # Modelo y vectorizador entrenados
│ │ ├── model.pkl
│ │ └── vectorizer.pkl
│ └── __init__.py
│
├── start_api.bat # Script para levantar la API en Windows
├── requirements.txt
└── README.md


---

## 🧠 Enfoque del modelo

- **Vectorización**: TF-IDF  
- **Modelo**: Regresión Logística  
- **Tipo de aprendizaje**: Supervisado  
- **Clases**: bug / consulta / feature  

Se utiliza `class_weight="balanced"` para reducir el sesgo en datasets pequeños.

---

## ⚙️ Entrenamiento

El modelo se entrena a partir de textos etiquetados manualmente.  
Durante el entrenamiento:

- El vectorizador aprende el vocabulario
- El modelo ajusta pesos por palabra
- El intercepto captura la tendencia global cuando no hay señales fuertes

El modelo **no memoriza textos**, aprende relaciones estadísticas entre palabras y categorías.

---

## 🌐 API (FastAPI)

La API expone un endpoint para clasificar texto.

### ▶️ Levantar la API (Windows)

Doble click en:

start_api.bat

O desde terminal:

python -m uvicorn src.api.app:app

---

La API queda disponible en:

http://127.0.0.1:8000/docs

---

### 📡 Endpoint

POST /predict

Input

{
  "texto": "error al guardar usuario"
}

Output

{
  "categoria": "bug",
  "probabilidades": {
    "bug": 0.72,
    "consulta": 0.18,
    "feature": 0.10
  }
}

---

### 🔍 Interpretabilidad

El modelo permite inspeccionar:

pesos por palabra (modelo.coef_)

influencia de términos específicos

probabilidades por clase (predict_proba)

Esto facilita entender por qué se toma cada decisión.

---

### ⚠️ Limitaciones

Dataset pequeño

Palabras no vistas se ignoran

El rendimiento mejora principalmente con más datos, no con más código

---

### 🚀 Próximos pasos

Aumentar el dataset

Agregar evaluación formal (accuracy, confusion matrix)

Usar n-grams

Dockerizar la API

Deploy en la nube

---

### 📌 Conclusión

Este proyecto demuestra un pipeline completo de Machine Learning:

procesamiento de texto

entrenamiento

interpretación

exposición como API

Pensado como base para sistemas reales de clasificación automática.

