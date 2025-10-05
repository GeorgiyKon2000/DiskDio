# 💽 Disk Usage Chart

A simple Python tool that scans all mounted disks on your system and visualizes their used and free space with colorful pie charts.  
Works on **Windows, Linux, and macOS**.

---

## 📦 Features
- Automatically detects all drives and partitions.  
- Displays total, used, and free space for each disk.  
- Generates clean pie charts using `matplotlib`.  
- Cross-platform and lightweight.

---

## 🖥️ Example Output

📊 Disk usage information:
C:\ — 238.47 GB total, 120.56 GB used, 117.91 GB free.
D:\ — 931.51 GB total, 720.45 GB used, 211.06 GB free.

Then a pie chart will appear for each disk.

---

## ⚙️ Installation


1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/disk-usage-chart.git
   cd disk-usage-chart
2. **(Optional but recommended) Create and activate a virtual environment:**
   python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Linux/macOS:
    source venv/bin/activate
3. **Install the dependencies:**
    pip install -r requirements.txt

---

## 🧩 Requirements

Just in requirements.txt

print in your terminal:

pip install -r requirements.txt

---

## 🚀 Run the program

python disk_usage_chart.py

---

## 🧠 Future ideas

- Add bar charts to compare all disks at once.

- Export data to JSON or CSV.

- Add GUI with tkinter or PyQt.

---

## 📜 License

This project is licensed under the MIT License — feel free to use, modify, and share it.

