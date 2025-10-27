# Static Code Analysis — Inventory Management System

## 👤 Student Details
**Name:** Adarsh V  
**SRN:** PES2UG23CS026    

---

## 🎯 Objective
The objective of this lab is to understand the importance of **static code analysis** in improving software quality.  
This project applies tools like **Pylint**, **Flake8**, and **Bandit** to a Python-based **Inventory Management System** to identify and fix:
- Code style violations (PEP8)
- Logical and runtime errors
- Security vulnerabilities

---

## 🧰 Tools Used
| Tool | Purpose |
|------|----------|
| **Python 3** | Programming language used |
| **Pylint** | Code quality and convention checker |
| **Flake8** | Style guide enforcement tool (PEP8) |
| **Bandit** | Security vulnerability scanner |
| **GitHub Codespaces** | Cloud development environment |
| **VS Code** | Code editor used for development |

---

## 📝 Summary of Work
1. Implemented a Python-based **Inventory Management System** with functionalities to:
   - Add and update inventory items  
   - Track stock quantities and generate reports  
   - Log all activities for auditing  
2. Performed static analysis using **Pylint**, **Flake8**, and **Bandit**.  
3. Fixed all identified issues related to:
   - Naming conventions  
   - File handling and exception safety  
   - Mutable default arguments  
   - Missing docstrings and inconsistent formatting  
   - Insecure use of `eval()`  
4. Generated detailed reports for all tools and verified improvements in readability, maintainability, and security.

---

## ⚙️ How to Run
```bash
# Clone the repository
git clone https://github.com/adarshv1025/SE-LAB5-Static-Code_Analysis.git
cd SE-LAB5-Static-Code_Analysis

# Install tools
pip install pylint flake8 bandit

# Run the program
python3 inventory_system.py
 ```
## Final Result ]
The inventory_system.py now passes all static analysis checks with a perfect score. 
* *Pylint Score:* *10.00/10* 
* *Bandit Report:* No issues identified.
* *Flake8 Report:* No issues identified.
