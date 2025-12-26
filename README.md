# 📘 AI Study Productivity Analyzer

An AI-powered web application that analyzes students’ study habits and predicts productivity using machine learning and behavioral analytics. The system provides actionable insights through an interactive dashboard to help users improve focus, consistency, and overall academic performance.

---

## 🚀 Problem Statement

Many students study for long hours but still struggle with low productivity due to poor focus, ineffective break patterns, distractions, and inconsistent study timings. There is no simple tool that helps students measure, understand, and improve their study productivity using data-driven insights.

---

## 💡 Solution Overview

The **AI Study Productivity Analyzer** collects study behavior inputs (study time, breaks, focus, distractions, and study hour) and uses a trained machine learning model to predict a **productivity score (0–100)**.

The system visualizes productivity trends, identifies the most productive study hours, and provides weekly insights through a clean, modern dashboard.

---

## ✨ Key Features

- 📊 Productivity prediction using Machine Learning  
- ⏰ Time-based intelligence (hour of study & weekday patterns)  
- 📈 Interactive dashboard with charts and KPIs  
- 🧠 Smart insights (best study time, productivity health)  
- 📅 Weekly performance summary  
- 💾 Persistent data storage (CSV-based logging)  
- 🎨 Modern SaaS-style UI (Tailwind CSS)  

---

## 🧠 Machine Learning Approach

- **Model Used:** Random Forest Regressor  
- **Why Random Forest?**
  - Handles non-linear patterns effectively
  - Performs well on small datasets
  - Captures complex interactions between behavioral features  

### Input Features
- Study minutes  
- Break minutes  
- Focus level (1–5)  
- Number of distractions  
- Hour of study  
- Day of week  

### Output
- Predicted productivity score (0–100)

---

## 🏗️ System Architecture

User Input (Web UI)
↓
Flask Backend
↓
ML Model (Random Forest)
↓
Productivity Score Prediction
↓
CSV Storage + Analytics
↓
Interactive Dashboard (Charts & Insights)


---

## 🛠️ Tech Stack

### Frontend
- HTML  
- Tailwind CSS  
- Chart.js  

### Backend
- Python  
- Flask  

### Machine Learning
- Scikit-learn  
- Pandas  
- NumPy  

### Data Storage
- CSV (can be upgraded to a database)

---

## 📁 Project Structure

study-productivity-ai/
│
├── app.py
├── model/
│ ├── productivity_model.pkl
│ └── train_model.py
│
├── data/
│ └── study_logs.csv
│
├── templates/
│ ├── index.html
│ └── dashboard.html
│
├── utils/
│ └── score_calculator.py
│
├── requirements.txt
└── README.md


---

## 📈 Dashboard Insights

- Total study sessions  
- Average productivity score  
- Latest productivity score  
- Weekly average productivity  
- Best study time recommendation  
- Productivity trend over time  
- Focus distribution (High / Medium / Low)  

---

## ⚠️ Limitations

- Trained on limited user-generated data  
- Productivity score is predictive, not absolute  
- Accuracy improves with more data  

---

## 🔮 Future Scope

- User authentication and profiles  
- Subject-wise productivity analysis  
- Mobile app version  
- Database integration (PostgreSQL / MongoDB)  
- Time-series forecasting for future productivity  
- AI-powered personalized study plans  

---

## 🎯 Use Cases

- Students preparing for exams  
- Self-learners and online course students  
- EdTech analytics platforms  
- Productivity and habit-tracking applications  

---

## 🏆 Why This Project Stands Out

- Combines Machine Learning with product thinking  
- Solves a real-world, relatable problem  
- End-to-end implementation (ML + Web + UI)  
- Clean, professional dashboard  
- Easy to explain in interviews  

---

## ⭐ How to Run the Project

```bash
pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000

📌 Author

Om Ahuja
B.Tech – Artificial Intelligence & Machine Learning
Portfolio: https://omahujaa.vercel.app/

⭐ If you like this project, give it a star!




