# 🚀 AutoTest Nexus

## 📌 Overview

AutoTest Nexus is a scalable automation testing framework built in Python that supports both **UI and API testing**.
It follows industry-standard QA practices including **test case design, bug reporting, and test execution reporting**, making it a complete testing solution suitable for real-world applications.

---

## 🧪 Key Features

* 🌐 UI Automation using Selenium WebDriver
* 🔌 API Testing using Python `requests`
* 🧱 Page Object Model (POM) for maintainable and scalable design
* ⚡ Parallel execution using `pytest-xdist`
* 🔁 Retry mechanism for handling flaky tests
* 🧠 Custom validation utilities for flexible assertions
* 📊 HTML reporting using PyTest
* 📄 QA documentation (Test Cases, Bug Reports, Test Reports)

---

## 🛠 Tech Stack

* Python
* Selenium
* PyTest
* Requests
* PyTest Plugins (xdist, html, rerunfailures)

---

## 📁 Project Structure

```
autotest-nexus/
│
├── tests/            # Test cases (UI + API)
├── pages/            # Page Object Model classes
├── api/              # API client layer
├── utils/            # Helper utilities
├── assets/           # Screenshots (reports/output)
├── docs/             # QA documentation
│   ├── test_cases.md
│   ├── bug_report.md
│   └── test_report.md
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```
git clone https://github.com/Srishti-04/AutoTest-Nexus.git
cd AutoTest-Nexus
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Tests

```
pytest
```

### 5️⃣ Run Tests in Parallel

```
pytest -n auto
```

### 6️⃣ Run with Retry Mechanism

```
pytest --reruns 2
```

---

## 📸 Test Execution Report

Below is a sample HTML report generated after running the test suite:

![Test Report](assets/report.png)

---

## 📄 QA Documentation

This project includes complete QA artifacts:

* **Test Cases** → `docs/test_cases.md`
* **Bug Reports** → `docs/bug_report.md`
* **Test Execution Report** → `docs/test_report.md`

---

## 🎯 Use Cases

* Functional UI testing of web applications
* Backend API validation
* Regression testing
* Demonstration of complete QA workflow

---

## 📈 Future Enhancements

* CI/CD integration (Jenkins / GitHub Actions)
* Dockerized execution
* Advanced reporting dashboards
* Integration with test management tools

---

## 👨‍💻 Author

Srishti Jaiswal

---
