
# 💳 K-Nearest Neighbor (KNN) Loan Eligibility Prediction

A Streamlit-based web application that uses the K-Nearest Neighbors algorithm to predict loan eligibility based on user financial and demographic data.

---

## 🚀 Features
- Interactive web interface built with **Streamlit**
- Predicts loan eligibility using a pre-trained **KNN model**
- Real-time input form for age, income, job, and loan details
- 3D visualization of simulated KNN data using **Plotly**
- Clean, responsive layout with modern UI

---

## 🧠 Tech Stack
- **Python 3.12+**
- **Streamlit** – Frontend & dashboard framework  
- **Plotly** – Interactive visualization  
- **Scikit-learn** – Machine learning model  
- **Pandas & NumPy** – Data processing  

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/loan-eligibility-knn-app.git
   cd loan-eligibility-knn-app
````

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run knn_pinjaman.py
   ```

---

## 📂 File Structure

```
📁 loan-eligibility-knn-app
├── knn_pinjaman.py             # Main Streamlit app
├── knn_pinjam_mod.pkl          # Trained KNN model file
├── requirements.txt            # Dependencies list
└── README.md                   # Project documentation
```

---

## 📊 Example Screenshot

*(Add an image here once your app is running, e.g. `screenshot.png`)*

---

## 🧩 Future Improvements

* Add dataset upload feature for retraining
* Include more visual insights (loan trends, distributions)
* Add multiple ML models for comparison

---
