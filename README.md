# 🚀 AutoTest Nexus

## 📌 Overview

AutoTest Nexus is a scalable automation testing framework built in Python that supports both **UI and API testing**.
The project follows industry-standard QA practices, including **test case design, bug reporting, and test execution reporting**, making it a complete testing solution.

---

## 🧪 Key Features

* 🌐 UI Automation using Selenium
* 🔌 API Testing using Python `requests`
* 🧱 Page Object Model (POM) for maintainable test design
* ⚡ Parallel execution using pytest-xdist
* 🔁 Retry mechanism for flaky tests
* 🧠 Smart validation utilities for flexible assertions
* 📊 HTML reporting using PyTest
* 📄 QA documentation (Test Cases, Bug Reports, Test Reports)

---

## 🛠 Tech Stack

* Python
* Selenium
* PyTest
* Requests

---

## 📁 Project Structure

```id="m6g9s1"
autotest-nexus/
│
├── tests/            # Test cases (UI + API)
├── pages/            # Page Object Models
├── api/              # API client layer
├── utils/            # Reusable utilities
├── docs/             # QA documentation (test cases, bug reports, reports)
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```id="r8x2kp"
pip install -r requirements.txt
```

### 2️⃣ Run tests

```id="c5n1az"
pytest
```

### 3️⃣ Run in parallel

```id="t4y8qs"
pytest -n auto
```

### 4️⃣ Run with retry

```id="y2p7vl"
pytest --reruns 2
```

---

## 📄 QA Documentation

This project includes essential QA artifacts:

* **Test Cases** → `docs/test_cases.md`
* **Bug Reports** → `docs/bug_report.md`
* **Test Execution Reports** → `docs/test_report.md`

---

## 📊 Sample Output

* Generates HTML report after execution
* Displays pass/fail status for each test

---

## 🎯 Use Cases

* Web application testing (UI flows)
* Backend API validation
* Regression testing
* QA process demonstration (documentation + execution)

---

## 📈 Future Enhancements

* CI/CD integration (Jenkins / GitHub Actions)
* Docker-based execution
* Advanced reporting dashboards

---

## 👨‍💻 Author

Srishti Jaiswal

---
