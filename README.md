# 🎣 Phishing Website Detection Tool

A powerful GUI-based tool that detects whether a URL is phishing or legitimate using machine learning techniques. Created as part of the **RISE Internship – Cybersecurity & Ethical Hacking Project**.


## 📌 Problem Statement

Phishing websites often trick users into entering sensitive personal data, leading to identity theft and financial loss. This tool flags suspicious URLs to help users avoid phishing traps.


## 🎯 Objective

To build a lightweight script using rule-based features and a machine learning model (Random Forest Classifier) that predicts if a URL is **phishing** or **safe**.


## 💡 Features

- ✅ Detects phishing URLs using Random Forest ML algorithm
- 🔍 Analyzes advanced features (length, subdomains, @ symbol, etc.)
- 📊 Shows model accuracy
- 🖥️ Clean GUI built with Tkinter
- 💬 Gives detailed explanation for phishing detections
- 🧹 "Clear" button to reset input


## 🛠️ Technologies Used

- Python
- Tkinter (for GUI)
- Pandas
- Scikit-learn (Random Forest Classifier)
- Regex (for URL pattern analysis)



## 📂 Requirements

Install the required libraries using:

```bash
pip install pandas scikit-learn
