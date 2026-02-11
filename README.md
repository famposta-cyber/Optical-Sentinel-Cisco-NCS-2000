![CI Status](https://github.com/SEU_USUARIO_AQUI/Optical-Sentinel/actions/workflows/ci.yml/badge.svg)

# Optical-Sentinel: Automated Health-Check & Observability

> **Enterprise-grade Automation Solution for Preventive Monitoring in High-Capacity DWDM Optical Networks (Cisco NCS 2000).**

[🇧🇷 Clique aqui para a versão em Português](README.pt-br.md)

This project modernizes the management of critical telecommunications infrastructure. It replaces manual data collection processes via legacy protocols with an automated data pipeline, delivering real-time observability and proactive detection of physical network failures.

---

## 🎯 Business Value
* **Efficiency:** Reduces network health inspection time from hours to seconds.
* **Proactivity:** Detects signal degradation (dBm) before a service interruption (SLA breach) occurs.
* **Compliance:** Automated physical inventory auditing to prevent errors in asset databases (CMDB).

---

## 🏗️ Solution Architecture
1. **Data Source:** Simulation of real Cisco NCS 2000 logs via TL1 protocol.
2. **Processing Layer:** Python engine using Named Regex for data normalization.
3. **Storage:** PostgreSQL persistence for historical analysis.
4. **Observability:** Dynamic Metabase dashboards.
