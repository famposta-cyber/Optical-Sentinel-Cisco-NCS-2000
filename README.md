🛰️ Optical-Sentinel: Automated Health-Check & Observability
Automation Solution for Preventive Monitoring in DWDM Optical Networks (Cisco NCS 2000).

This project modernizes the management of critical telecommunications infrastructure. It replaces manual data collection processes via legacy protocols with an automated data pipeline, delivering real-time observability and proactive detection of physical failures.

🎯 Business Value (The "Sentinel" Effect)
In high-capacity networks (Core/Transport), a fiber outage can impact millions of users or critical industrial operations.

Efficiency: Reduces network health inspection time from hours to seconds.

Proactivity: Detects signal degradation (dBm) before a service interruption (SLA breach) occurs.

Compliance: Automated physical inventory auditing to prevent errors in asset databases (CMDB).

🏗️ Solution Architecture
The pipeline was designed following DevNet and SecDevOps principles:

Data Source (Mocking): Simulation of real Cisco NCS 2000 logs via the TL1 (Transaction Language 1) protocol.

Processing Layer (Python): Parsing engine using Named Regex to transform unstructured data into structured JSON objects.

Storage (PostgreSQL): Relational database persistence for historical analysis and trend reporting.

Security (SecDevOps): Secret and credential management via environment variables (.env).

Intelligence: Thresholding logic for generating critical alerts in the console.

Observability (Metabase): Dynamic dashboard for technical and executive visualization.

🛠️ Tech Stack
Language: Python 3.12+ (Regex, JSON, psycopg2, python-dotenv)

Infrastructure: Docker & Docker Compose

Database: PostgreSQL 15-Alpine

Visualization: Metabase BI

Automation: Ansible (Workflow Orchestration)

🚀 How to Run
1. Environment Setup
Clone the repository and ensure Docker is running:
```bash
docker-compose up -d
============================================================================================================================================================================================================
# 🛰️ Optical-Sentinel: Automated Health-Check & Observability

> **Solução de Automação para Monitoramento Preventivo em Redes Ópticas DWDM (Cisco NCS 2000).**

Este projeto moderniza a gestão de infraestruturas críticas de telecomunicações. Ele substitui processos manuais de coleta de dados via protocolos legados por um pipeline de dados automatizado, entregando observabilidade em tempo real e detecção proativa de falhas físicas.

---

## 🎯 Valor de Negócio (The "Sentinel" Effect)

Em redes de alta capacidade (Core/Transporte), uma queda de fibra pode impactar milhões de usuários ou operações industriais críticas.

* **Eficiência:** Redução do tempo de inspeção de saúde da rede de horas para segundos.
* **Proatividade:** Detecção de degradação de sinal (dBm) antes que ocorra a interrupção do serviço (SLA).
* **Conformidade:** Auditoria automatizada de inventário físico para evitar erros em bases de ativos (CMDB).

---

## 🏗️ Arquitetura da Solução

O pipeline foi desenhado seguindo princípios de **DevNet** e **SecDevOps**:

1.  **Data Source (Mocking):** Simulação de logs reais do Cisco NCS 2000 via protocolo **TL1 (Transaction Language 1)**.
2.  **Processing Layer (Python):** Motor de parsing utilizando **Regex Nomeada** para transformar dados não estruturados em objetos JSON.
3.  **Storage (PostgreSQL):** Persistência em banco de dados relacional para análise histórica e tendências.
4.  **Security (SecDevOps):** Gestão de segredos e credenciais via variáveis de ambiente (`.env`).
5.  **Intelligence:** Lógica de *Thresholding* para geração de alertas críticos no console.
6.  **Observability (Metabase):** Dashboard dinâmico para visualização técnica e executiva.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.12+ (Regex, JSON, `psycopg2`, `python-dotenv`)
* **Infraestrutura:** Docker & Docker Compose
* **Banco de Dados:** PostgreSQL 15-Alpine
* **Visualização:** Metabase BI
* **Automação:** Ansible (Orquestração de Workflow)

---

## 🚀 Como Executar

### 1. Preparação do Ambiente
Clone o repositório e garanta que o Docker esteja rodando:
```bash
docker-compose up -d
