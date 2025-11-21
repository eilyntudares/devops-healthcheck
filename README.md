# DevOps Healthcheck 🔧
A lightweight DevOps-style healthcheck system that monitors service availability using **Python**, **YAML**, and **GitHub Actions**. It sends HTTP requests, measures latency, and generates a JSON report — fully automated through a CI/CD pipeline.

---

## 🚀 Features
- Reads service definitions from `services.yaml`
- Sends HTTP GET requests to each service
- Measures response time (latency)
- Marks services as **healthy** or **unhealthy** based on:
  - Expected HTTP status code
  - Maximum allowed latency
- Generates a clean `health_report.json`
- Fully automated through **GitHub Actions**
  - Runs on **every push**
  - Runs on a **daily schedule** via cron
- Uploads the latest report as a build artifact

---

## 🧩 Project Structure
```
devops-healthcheck/
│
├── healthcheck.py          # Main healthcheck script
├── services.yaml           # List of services to monitor
├── requirements.txt        # Python dependencies
├── health_report.json      # Latest report (auto-generated)
└── .github/
    └── workflows/
        └── healthcheck.yml # CI/CD pipeline
```

---

## 🛠️ Technologies Used
- **Python 3**
- **requests** — HTTP requests
- **PyYAML** — YAML config parsing
- **GitHub Actions** — CI/CD automation
- **Cron** — scheduled daily runs

---

## 💻 Running the Project Locally

### 1️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the script manually
```bash
python3 healthcheck.py
```
This will generate a new `health_report.json`.

---

## ⚙️ GitHub Actions (CI/CD)
The workflow performs the following on every run:
- Sets up Python
- Installs project dependencies
- Executes the healthcheck script
- Uploads the JSON report as an artifact

### Runs automatically:
✔️ On every push  
✔️ Daily at **06:00 UTC**  

You can view logs and artifacts in the **Actions** tab of the repository.

---

## 📈 Future Improvements
- Slack or email alerts for unhealthy services  
- Dockerize the project  
- Support for additional HTTP methods (`POST`, `PUT`, etc.)  
- Store historical reports (e.g., AWS S3)  
- Build a small HTML dashboard for visualization  

---

## 📚 Purpose of This Project
This project was created to practice real DevOps engineering concepts:
- Monitoring & automation  
- CI/CD pipelines  
- Scheduling jobs  
- Configuration-as-code  
- Lightweight service health verification  

It demonstrates how to continuously monitor service health using Python and GitHub Actions.
