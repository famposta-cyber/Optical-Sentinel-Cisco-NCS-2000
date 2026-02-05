# Optical-Sentinel: Automated Health-Check & Observability
> **Automation Solution for Preventive Monitoring in DWDM Optical Networks (Cisco NCS 2000).**

This project modernizes the management of critical telecommunications infrastructure. It replaces manual data collection processes via legacy protocols with an automated data pipeline, delivering real-time observability and proactive detection of physical failures.

---

## Business Value (The "Sentinel" Effect)

In high-capacity networks (Core/Transport), a fiber outage can impact millions of users or critical industrial operations.

* **Efficiency: Reduces network health inspection time from hours to seconds.

* **Proactivity: Detects signal degradation (dBm) before a service interruption (SLA breach) occurs.

* **Compliance: Automated physical inventory auditing to prevent errors in asset databases (CMDB).

## Solution Architecture
The pipeline was designed following **DevNet** and **SecDevOps principles**:

1. **Data Source (Mocking):** Simulation of real Cisco NCS 2000 logs via the **TL1 (Transaction Language 1) protocol**.

2. **Processing Layer (Python):** Parsing engine using **Named Regex** to transform unstructured data into structured JSON objects.

3. **Storage (PostgreSQL):** Relational database persistence for historical analysis and trend reporting.

4. **Security (SecDevOps):** Secret and credential management via environment variables (.env).

5. **Intelligence:** *Thresholding* logic for generating critical alerts in the console.

6. **Observability (Metabase):** Dynamic dashboard for technical and executive visualization.

## Tech Stack
* **Language: Python 3.12+ (Regex, JSON, psycopg2, python-dotenv)

* **Infrastructure: Docker & Docker Compose

* **Database: PostgreSQL 15-Alpine

* **Visualization: Metabase BI

* **Automation: Ansible (Workflow Orchestration)

## How to Run
1. Environment Setup
Clone the repository and ensure Docker is running:
```bash
docker-compose up -d