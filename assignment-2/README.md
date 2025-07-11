# ⚡ Power System Load Type Prediction Using Machine Learning

This project develops a machine learning pipeline to predict the **Load Type** of a power system based on historical energy consumption and power factor data. The goal is to classify the load as **Light Load**, **Medium Load**, or **Maximum Load** using a mix of time-series and environmental features.

---

## 🧩 Problem Statement

Accurately classify the **Load_Type** of a power system using the following features:

- 📅 Date and Time  
- ⚡ Usage (kWh)  
- 🔌 Lagging/Leading Current Reactive Power (kVarh)  
- 🌫️ CO₂ Emissions (ppm)  
- 🕒 NSM (Number of Seconds from Midnight)  

**Target Classes**:
- `Light Load`
- `Medium Load`
- `Maximum Load`

---

## 🛠️ Methodology

### 1. Data Preprocessing
- Parsed datetime column
- Handled missing values using median imputation
- Scaled numerical features using `StandardScaler`

### 2. Exploratory Data Analysis (EDA)
- Distribution plots (histogram, boxplot, violin)
- Correlation heatmap
- Time-based patterns (hourly and monthly)

### 3. Feature Engineering
- Time-based features: `Hour`, `Month`, `Is_Peak_Hour`, `Is_Weekend`
- Log-transformed skewed features (`CO₂`, `Usage`)
- Final feature set creation

### 4. Time-based Train/Test Split
- Used the **last month** as the test set
- Ensured chronological split to prevent data leakage

### 5. Model Training
- `Random Forest Classifier`
- `Logistic Regression`

### 6. Evaluation Metrics
- Accuracy
- Precision, Recall
- **F1 Score (macro)**
- Confusion Matrix
- Feature Importance

### 7. Model Comparison
- Compared performance using F1 Score
- Bar charts and confusion matrix for visualization

---

## ✅ Results

- **Random Forest** achieved the best F1-score and performance consistency across all classes.
- **Logistic Regression** provided a simple yet interpretable baseline.
- Time-based validation ensured robustness on future data.

---

## 📊 Key Insights

- Load patterns vary by **hour** and **CO₂ levels**
- `NSM` and `Usage` are top predictors
- Time-based split prevents information leakage and ensures realistic evaluation

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

**Required libraries:**
- `pandas`
- `numpy`
- `scikit-learn`
- `seaborn`
- `matplotlib`

---

## 🚀 Usage

Run the components in this order:

```bash
# Step 1: Preprocessing
python preprocessing.py

# Step 2: Run EDA notebook
jupyter notebook eda.ipynb

# Step 3: Model Training
python model_training.py

# Step 4: Evaluation
python evaluation.py

# Step 5: Feature Importance
python feature_importance.py

# Step 6: Compare Models
python model_comparison.py
```

---

## 📁 Project Structure

```
.
├── preprocessing.py
├── eda.ipynb
├── model_training.py
├── evaluation.py
├── feature_importance.py
├── model_comparison.py
├── requirements.txt
└── README.md
```

---

## 🔚 Conclusion

This project showcases an end-to-end machine learning pipeline with careful attention to time-based validation, feature engineering, and interpretability. The trained model can serve as a basis for power system monitoring and intelligent energy usage prediction in real-world environments.

---
