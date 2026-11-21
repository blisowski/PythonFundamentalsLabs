<div align="center">

# 🐍 Python Fundamentals Labs

**Practical Python exercises | Postgraduate Studies in Cloud Computing IT Solutions Architecture**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Learning](https://img.shields.io/badge/Focus-Python%20Fundamentals-2E8B57)
![Status](https://img.shields.io/badge/Status-In%20Progress-F4A261)

*A collection of hands-on exercises documenting my progress in learning Python and building a foundation for cloud-oriented software development and automation.*

</div>

## 📖 About the Project

This repository contains Python programming labs and practical assignments completed as part of my **postgraduate studies in Cloud Computing IT Solutions Architecture**.

The goal is to strengthen core programming skills through small, focused examples. The current exercises use a simple sales scenario to explore Python syntax, data types, control flow, functions, and data structures. These fundamentals are also useful when working with automation, scripting, and cloud-based solutions.

> **Scope:** The examples currently focus on Python fundamentals. They do not yet implement or deploy cloud infrastructure.

## 📂 Repository Structure

```text
PythonFundamentalsLabs/
├── .gitignore
├── Exercise1_sales.py       # Variables, calculations, conditions, and loops
├── Exercise2_functions.py   # Functions, type conversion, lists, and dictionaries
└── README.md
```

## 🧪 Exercises

### 01 — Sales Basics

**File:** [`Exercise1_sales.py`](./Exercise1_sales.py)

Introduces basic Python constructs using a product sales example.

**Topics covered:**
- Variables and built-in types: `str`, `int`, `float`, and `bool`
- Printing values and inspecting types with `type()`
- Arithmetic operations to calculate total sales
- Conditional logic with `if` / `else`
- Iterating over a list with a `for` loop
- Comparing sales amounts against a target

**Example:**

```python
product = "Laptop"
quantity = 5
unitPrice = 1650.00

totalSales = quantity * unitPrice
# 8250.0
```

The exercise checks whether the calculated sales total meets a **2,000** target and then evaluates individual amounts in a list against the same threshold.

### 02 — Functions and Data Structures

**File:** [`Exercise2_functions.py`](./Exercise2_functions.py)

Builds on the first exercise by introducing reusable logic and common data structures.

**Topics covered:**
- Defining and calling functions with parameters
- Reusing a calculation with different inputs
- Converting a numeric string to an integer using `int()`
- Working with lists, indexing, and `len()`
- Storing structured data in dictionaries
- Accessing dictionary values by key

**Example:**

```python
def calculate_sales(quantity, unitPrice):
    return quantity * unitPrice

order = {
    "OrderID": "ORD001",
    "Product": "Laptop",
    "Quantity": 2,
    "UnitPrice": 850,
}

total = calculate_sales(order["Quantity"], order["UnitPrice"])
# 1700
```

The function is also called with multiple combinations of quantities and unit prices, demonstrating how reusable code reduces repetition.

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed and available from the terminal
- **Git** to clone the repository (or download the source files directly)

The current exercises use only Python built-in functionality, so **no third-party packages or `pip install` steps are required**.

### Clone the Repository

```bash
git clone https://github.com/blisowski/PythonFundamentalsLabs.git
cd PythonFundamentalsLabs
```

### Run the Exercises

Run each script independently:

```bash
python Exercise1_sales.py
python Exercise2_functions.py
```

On systems where Python 3 is invoked as `python3`, use:

```bash
python3 Exercise1_sales.py
python3 Exercise2_functions.py
```

Both scripts print their results directly to the terminal. No input files, environment variables, or cloud credentials are needed.

## 🎯 Learning Objectives

| Area | Skills practiced |
| --- | --- |
| Python basics | Variables, primitive types, output, and arithmetic |
| Control flow | Conditional statements, comparisons, and loops |
| Functions | Defining reusable operations and passing arguments |
| Data handling | Lists, dictionaries, indexing, and type conversion |
| Problem solving | Translating a simple business scenario into executable logic |

## ☁️ Connection to Cloud Computing

Python is widely used for scripting and automation in cloud environments. The skills practiced here provide a starting point for future work involving:

- Automation and operational scripts
- Working with structured configuration and API data
- Cloud service integration
- Infrastructure and deployment tooling

These are **potential applications of the skills being learned**, not features currently implemented in this repository.

## 📈 Project Evolution

This is a learning repository. Additional labs may be added as the postgraduate course progresses, with each exercise documenting a new concept or practical technique.

## 👤 Author

**Bartosz Lisowski**  
GitHub: [@blisowski](https://github.com/blisowski)

---

<div align="center">

*Created for educational purposes as part of postgraduate studies in Cloud Computing IT Solutions Architecture.*

</div>
