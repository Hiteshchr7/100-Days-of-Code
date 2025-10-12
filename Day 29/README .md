# Day 29 - Password Manager GUI App

This is a simple **Password Manager GUI Application** built using Python's `tkinter`.  
It allows you to generate secure random passwords, save them along with website and email details, and search for saved credentials.

---

## 🚀 Features
- Generate strong random passwords with letters, numbers, and symbols.
- Copy generated passwords automatically to clipboard.
- Save website, email, and password securely in a `data.json` file.
- Search functionality to quickly retrieve stored credentials.
- Simple and user-friendly GUI.

---

## 🛠️ Tech Stack
- Python 3
- Tkinter (GUI framework)
- JSON (for storing credentials)
- Pyperclip (for clipboard support)
- Random (for password generation)

---

## 📂 Project Structure
```
Day29/
│── Password Generator and Manager GUI.py          # Main application script
│── logo.png                                       # Application logo
│── data.json                                      # Stored credentials (auto-created on save)
│── README.md                                      # Project documentation
```

---

## ▶️ How to Run
1. Clone this repository or copy the files to your local system.
2. Install dependencies (if not already installed):
   ```bash
   pip install pyperclip
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## 📸 Screenshot
![alt text](logo.png)

---

## 📌 Notes
- If `data.json` does not exist, it will be created automatically when you save your first entry.
- Always keep a backup of your `data.json` file, as it stores all your saved credentials.

---

## ✅ Example Usage
1. Enter website, email, and password details OR generate a strong password.
2. Click **Add** to save credentials.
3. Use the **Search** button to retrieve stored details quickly.

---

## 📅 100 Days of Code - Day 29
This project is part of my **100 Days of Code Challenge** (Day 29).  
The focus of this project was to practice **GUI applications with Tkinter**, file handling with **JSON**, and **password generation logic**.
