# 🚀 AutoTest Nexus

## 📌 Overview

AutoTest Nexus is a scalable automation testing framework built in Python to support both **UI and API testing**.
It is designed with maintainability, reusability, and performance in mind, following industry best practices used by SDET engineers.

---

## 🧪 Key Features

* 🌐 UI Automation using Selenium
* 🔌 API Testing using Python `requests`
* 🧱 Page Object Model (POM) for clean architecture
* ⚡ Parallel test execution using pytest-xdist
* 🔁 Retry mechanism for handling flaky tests
* 🧠 Smart validation utilities for flexible assertions
* 📊 HTML test reporting using PyTest

---

## 🛠 Tech Stack

* Python
* Selenium
* PyTest
* Requests

---

## 📁 Project Structure

```
autotest-nexus/
│
├── tests/           # Test cases (UI + API)
├── pages/           # Page Object Models
├── api/             # API client layer
├── utils/           # Reusable utilities (validators)
├── conftest.py      # PyTest fixtures
├── pytest.ini       # PyTest configuration
├── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run tests

```
pytest
```

### 3️⃣ Run in parallel

```
pytest -n auto
```

### 4️⃣ Run with retry

```
pytest --reruns 2
```

---

## 📊 Sample Output

* Generates HTML report after execution
* Displays test results (pass/fail) with details

---

## 📈 Future Enhancements

* CI/CD integration (Jenkins / GitHub Actions)
* Docker-based execution
* Advanced reporting dashboards
* Performance testing integration

---

## 🎯 Use Case

This framework can be used to test:

* Web applications (UI flows)
* Backend APIs
* End-to-end workflows

---

## 👨‍💻 Author

Srishti Jaiswal

---
