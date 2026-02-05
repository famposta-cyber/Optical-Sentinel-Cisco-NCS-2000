-- Tabela para o Inventário de Hardware
CREATE TABLE IF NOT EXISTS optical_inventory (
    id SERIAL PRIMARY KEY,
    slot INT,
    model VARCHAR(50),
    vid VARCHAR(50),
    hw_rev VARCHAR(50),
    serial VARCHAR(100) UNIQUE,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela para Níveis de Potência (Telemetria)
CREATE TABLE IF NOT EXISTS optical_power (
    id SERIAL PRIMARY KEY,
    interface VARCHAR(50),
    power_value FLOAT,
    status VARCHAR(10),
    collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);