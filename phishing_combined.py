import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import re

# Step 1: Extract advanced features from URL
def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append('@' in url)  # Presence of @
    features.append(url.count('-'))  # Number of hyphens
    features.append(not url.startswith('https'))  # Not using https
    features.append(url.count('.') > 2)  # More subdomains
    features.append(bool(re.search(r'http[s]?://\d+\.\d+\.\d+\.\d+', url)))  # IP address in URL
    features.append(any(shortener in url for shortener in ['bit.ly', 'goo.gl', 'tinyurl', 'ow.ly']))  # Shortened URL
    return features

# Load dataset
dataset = pd.read_csv('phishing_dataset.csv')

# Prepare data
X = []
y = []

for index, row in dataset.iterrows():
    X.append(extract_features(row['URL']))
    y.append(1 if row['Label'] == 'phishing' else 0)

# Train Random Forest model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100

# GUI Function to Predict
def check_url():
    url = url_entry.get()
    if url.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a URL!")
        return

    features = extract_features(url)
    prediction = model.predict([features])[0]

    if prediction == 1:  # Phishing URL
        explanation = []
        if len(url) > 75:
            explanation.append("🚨 URL length is too long.")
        if '@' in url:
            explanation.append("🚨 URL contains '@' symbol.")
        if url.count('-') > 3:
            explanation.append("🚨 URL contains many hyphens.")
        if not url.startswith('https'):
            explanation.append("🚨 URL does not use HTTPS.")
        if url.count('.') > 2:
            explanation.append("🚨 URL contains multiple subdomains.")
        if bool(re.search(r'http[s]?://\d+\.\d+\.\d+\.\d+', url)):
            explanation.append("🚨 URL contains an IP address.")
        if any(shortener in url for shortener in ['bit.ly', 'goo.gl', 'tinyurl', 'ow.ly']):
            explanation.append("🚨 URL uses a shortening service.")

        result_box.config(bg="#ff4d4d")
        result_label.config(text="⚠️ Phishing URL Detected!", fg="white")

        explanation_text.config(state='normal')
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(tk.END, "\n".join(explanation))
        explanation_text.config(state='disabled')

    else:  # Safe URL
        result_box.config(bg="#27ae60")
        result_label.config(text="✅ This URL is Safe.", fg="white")

        explanation_text.config(state='normal')
        explanation_text.delete(1.0, tk.END)
        explanation_text.insert(tk.END, "✅ This URL seems completely safe. No suspicious features detected.")
        explanation_text.config(state='disabled')

def clear_input():
    url_entry.delete(0, tk.END)
    result_box.config(bg="#d9d9d9")
    result_label.config(text="")
    explanation_text.config(state='normal')
    explanation_text.delete(1.0, tk.END)
    explanation_text.config(state='disabled')

# Build GUI
window = tk.Tk()
window.title("Advanced Phishing URL Detection Tool")
window.geometry("750x600")
window.config(bg="#f0f4f7")

# Heading
tk.Label(window, text="Phishing URL Detection Tool", font=("Arial", 24, "bold"), fg="#2c3e50", bg="#f0f4f7").pack(pady=20)

# Accuracy display
tk.Label(window, text=f"Model Accuracy: {accuracy:.2f}%", font=("Arial", 14), fg="#27ae60", bg="#f0f4f7").pack(pady=5)

# URL input
tk.Label(window, text="Enter URL to Check:", font=("Arial", 14), bg="#f0f4f7").pack(pady=10)
url_entry = tk.Entry(window, width=60, font=("Arial", 14))
url_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(window, bg="#f0f4f7")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Check URL", command=check_url, font=("Arial", 12), bg="#3498db", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", command=clear_input, font=("Arial", 12), bg="#95a5a6", fg="white", width=15).grid(row=0, column=1, padx=10)

# Result box with border and color
result_box = tk.Frame(window, bg="#d9d9d9", width=400, height=50, highlightbackground="black", highlightthickness=1)
result_box.pack(pady=20)
result_label = tk.Label(result_box, text="", font=("Arial", 16, "bold"), bg="#d9d9d9")
result_label.pack(pady=10)

# Explanation label
tk.Label(window, text="Detailed Explanation:", font=("Arial", 14), bg="#f0f4f7").pack(pady=5)

explanation_text = tk.Text(window, width=80, height=10, font=("Arial", 12), wrap="word", state='disabled', bg="#ecf0f1", bd=2, relief="sunken")
explanation_text.pack(pady=10)

window.mainloop()




