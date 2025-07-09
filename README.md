# 🎵 Spotify Tracks Analyzer

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A Python project to analyze Spotify tracks dataset and visualize insights about genres and track popularity.

---

## 📊 Example Outputs

### 🎼 Top 10 genres by total popularity
![Top genres](images/top_genres.png)

### 📈 Popularity distribution
![Popularity distribution](images/popularity_distribution.png)

---

## 🚀 Features
- **Top 10 genres by total popularity**
- **Popularity distribution histogram**
- **Automatically saves graphs as PNG**
- **Clean modular project structure**

---

## 📦 Project Structure
```text
spotify-analyzer/
├── data/                      # Raw dataset (not included)
├── images/                    # Saved graphs
│   ├── top_genres.png
│   └── popularity_distribution.png
├── src/
│   └── analyzer.py
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/                     # Virtual environment (ignored)
⚙️ Installation
Clone the repository and set up the environment:

bash
Copy
Edit
git clone https://github.com/<your-username>/spotify-analyzer.git
cd spotify-analyzer
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Linux/Mac
pip install -r requirements.txt
▶️ Usage
Run the analysis script:

bash
Copy
Edit
python -m src.analyzer
This will:

Load the Spotify dataset

Generate and save two graphs in the images/ folder

Display the graphs in your system viewer

🛠 Technologies
Python 3.11

pandas

seaborn

matplotlib

📜 License
This project is licensed under the MIT License. See LICENSE for details.