# 🎓 Student Performance Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-Data%20Processing-green)
![Gradio](https://img.shields.io/badge/Gradio-Interactive%20UI-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An interactive analytics dashboard built using **NumPy** for data processing and **Gradio** for the web interface.

This project demonstrates real-world data cleaning, statistical analysis, ranking systems, and dashboard creation — all using vectorized NumPy operations (no loops).

---

## 🚀 Project Overview

The **Student Performance Analyzer** simulates exam data for students and performs:

- 📥 Data generation  
- 🧹 Missing value handling  
- 📊 Statistical analytics  
- 🏆 Ranking & performance insights  
- 🌐 Interactive web-based dashboard  

This project highlights intermediate-level NumPy proficiency combined with a clean UI using Gradio.

---

## ✨ Features

### 📥 Data Generation
- Generates synthetic student names
- Creates scores for 5 subjects
- Injects missing values (`-1`) intentionally

### 🧹 Data Cleaning
- Replaces missing values using **column-wise mean**
- Uses `np.nanmean()` for accurate imputation
- Fully vectorized implementation

### 📊 Student Analytics
- Average score per student
- Total score per student
- Standard deviation per student
- 🥇 Top 5 students (by total score)
- 📉 Bottom 5 students
- 🎯 Overall class average

---

## 🖥️ Demo Workflow

1. Generate student dataset  
2. Clean missing values  
3. Compute analytics  
4. View rankings and statistics in real time  

Everything updates interactively in the browser.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Core programming language |
| 🧮 NumPy | Data processing & vectorized computation |
| 🌐 Gradio | Interactive UI & dashboard |

---

## Author

Chinmay V Chatradamath.

---
