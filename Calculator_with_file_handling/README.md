# 📘 Simple CLI Calculator with History – Python 🧮

This is a command-line calculator written in Python that supports basic arithmetic operations (+, -, *, /) and maintains a history of calculations in a local file (`history.txt`). You can view, clear, and persist your calculation history easily.

## 🚀 Features

- Basic arithmetic operations: `+`, `-`, `*`, `/`
- Persistent history using `history.txt`
- Reverse chronological history display (most recent first)
- Clear history command
- User-friendly CLI interface

## 📂 Project Structure

📁 YourProjectFolder/
├── 📄 calculator.py # Main script with calculator logic
├── 📄 history.txt # Auto-created file to store history
└── 📄 README.md # Project documentation

## ⚙️ How to Use

1. **Run the script**:
   ```bash
   python calculator.py
Example:
Enter Expression(e.g 2+3(+,-,?,*)) or Commands(history,exit,clear): 5 + 2
7.0
Enter Expression(e.g 2+3(+,-,?,*)) or Commands(history,exit,clear): history
5 + 2 = 7.0
Enter Expression(e.g 2+3(+,-,?,*)) or Commands(history,exit,clear): clear
History Cleared Successfully!!!
