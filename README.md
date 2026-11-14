# 🏠 House Price Prediction System

An end-to-end machine learning web application that forecasts residential real estate valuations based on key property metrics. Built with a clean preprocessing pipeline and deployed live for real-time predictions.

🔗 **Live Demo:** https://house-price-predictor-web-page.vercel.app/

---

## 📌 Overview
Real estate pricing depends on multiple interacting variables such as property size, location attributes, and structural features. This project bridges the gap between statistical modeling and user accessibility by serving a trained regression model through an interactive web interface.

## ✨ Key Features
* **Real-Time Valuation:** Instant house price predictions directly from user-inputted property parameters.
* **Robust Preprocessing Pipeline:** Automated data cleaning, outlier removal, and feature scaling (`StandardScaler`) to maintain structural integrity across disparate inputs.
* **Responsive Web Interface:** Clean, lightweight UI built for seamless interaction across desktop and mobile devices.

---

## 🛠️ Tech Stack
* **Machine Learning & Data Science:** Python, Scikit-Learn, Pandas, NumPy
* **Preprocessing & Serialization:** `StandardScaler`, Outlier Extraction Pipelines
* **Frontend & Web:** HTML5, CSS3, JavaScript
* **Deployment:** Vercel

---

## ⚙️ Machine Learning Workflow
1. **Exploratory Data Analysis (EDA):** Analyzed feature distributions, correlations, and target price skewness.
2. **Data Cleaning & Outlier Removal:** Handled missing records and filtered statistical anomalies to prevent regression distortion.
3. **Feature Scaling:** Applied `StandardScaler` so numerical features contribute proportionally during model training and inference.
4. **Model Training & Evaluation:** Trained and evaluated regression models to deliver reliable continuous price forecasts.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd house-price-predictor-web-page-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
# Start your local server or open the web entry file
python app.py
```
*(Update the command above if your backend uses Flask/FastAPI or runs purely as a static frontend).*

---

## 👩‍💻 Author
**Sanju Devi S.**
* **GitHub:** https://github.com/sanjuseervii 
* **LinkedIn:** : https://www.linkedin.com/in/sanju-devi-s/
