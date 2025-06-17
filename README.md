# 📚 Attendance Management System

> A lightweight desktop GUI application for managing student attendance using Python and Tkinter.

---

## 🎯 Overview

The **Attendance Management System** is a Python-based application that helps manage student records and track daily attendance efficiently. Built with a user-friendly interface using Tkinter, it stores data in CSV files and supports adding students, marking attendance, and generating attendance reports.

---

## 🚀 Features

- Add student details with auto-generated roll numbers  
- View and manage all student records  
- Mark attendance using checkboxes  
- Generate attendance reports for today or yesterday  
- Calculate and display percentage attendance  
- Simple GUI with intuitive navigation  
- No external database — uses CSV files  

---

## 🛠️ Tech Stack

| Technology | Use                      |
|------------|---------------------------|
| Python     | Core application logic    |
| Tkinter    | GUI forms and menus       |
| CSV Module | Data storage and retrieval|
| datetime   | Date-based report logic   |

---

## 📁 Project Structure

📁 Attendance Management System/
├── menu.py # Main GUI application
├── Student.csv # Student details data
├── Attendance.csv # Daily attendance data
└── README.md # Project documentation


---

## ▶️ How to Run

1. Ensure Python 3 is installed
2. Open terminal in project directory
3. Run:
   
bash
   python menu.py


4.Use the GUI menus:

     Add/View Students
    Mark/View Attendance  

🔮 Future Improvements
      Support for multiple classes & sections
      Weekly/monthly/yearly reports
      Export reports to Excel or PDF
      Face recognition-based attendance marking
