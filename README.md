![CI Status](SUA_URL_AQUI/actions/workflows/ci.yml/badge.svg)

# Optical-Sentinel: Automated Health-Check & Observability

> **SoluÃ§Ã£o de AutomaÃ§Ã£o para Monitoramento Preventivo em Redes Ã“pticas DWDM (Cisco NCS 2000).**

Este projeto moderniza a gestÃ£o de infraestruturas crÃ­ticas de telecomunicaÃ§Ãµes. Ele substitui processos manuais de coleta de dados via protocolos legados por um pipeline de dados automatizado, entregando observabilidade em tempo real e detecÃ§Ã£o proativa de falhas fÃ­sicas.

---

## Valor de NegÃ³cio (The "Sentinel" Effect)

Em redes de alta capacidade (Core/Transporte), uma queda de fibra pode impactar milhÃµes de usuÃ¡rios ou operaÃ§Ãµes industriais crÃ­ticas.

* **EficiÃªncia:** ReduÃ§Ã£o do tempo de inspeÃ§Ã£o de saÃºde da rede de horas para segundos.
* **Proatividade:** DetecÃ§Ã£o de degradaÃ§Ã£o de sinal (dBm) antes que ocorra a interrupÃ§Ã£o do serviÃ§o (SLA).
* **Conformidade:** Auditoria automatizada de inventÃ¡rio fÃ­sico para evitar erros em bases de ativos (CMDB).

---

## Arquitetura da SoluÃ§Ã£o

O pipeline foi desenhado seguindo princÃ­pios de **DevNet** e **SecDevOps**:

1.  **Data Source (Mocking):** SimulaÃ§Ã£o de logs reais do Cisco NCS 2000 via protocolo **TL1 (Transaction Language 1)**.
2.  **Processing Layer (Python):** Motor de parsing utilizando **Regex Nomeada** para transformar dados nÃ£o estruturados em objetos JSON.
3.  **Storage (PostgreSQL):** PersistÃªncia em banco de dados relacional para anÃ¡lise histÃ³rica e tendÃªncias.
4.  **Security (SecDevOps):** GestÃ£o de segredos e credenciais via variÃ¡veis de ambiente (`.env`).
5.  **Intelligence:** LÃ³gica de *Thresholding* para geraÃ§Ã£o de alertas crÃ­ticos no console.
6.  **Observability (Metabase):** Dashboard dinÃ¢mico para visualizaÃ§Ã£o tÃ©cnica e executiva.

---

## Stack TecnolÃ³gica

* **Linguagem:** Python 3.12+ (Regex, JSON, `psycopg2`, `python-dotenv`)
* **Infraestrutura:** Docker & Docker Compose
* **Banco de Dados:** PostgreSQL 15-Alpine
* **VisualizaÃ§Ã£o:** Metabase BI
* **AutomaÃ§Ã£o:** Ansible (OrquestraÃ§Ã£o de Workflow)

---

## Como Executar

### 1. PreparaÃ§Ã£o do Ambiente
Clone o repositÃ³rio e garanta que o Docker esteja rodando:
```bash
docker-compose up -d

