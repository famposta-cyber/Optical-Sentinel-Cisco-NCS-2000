import os
import re
import json
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class OpticalParser:
    """Responsável pela extração e normalização de dados brutos (NCS 2000 TL1)."""
    
    def __init__(self):
        # Regex Nomeada: Captura Slot, Modelo, VID, HW Rev e Serial
        self.inventory_pattern = r'"SLOT-(?P<slot>\d+):(?P<model>[^,]+),(?P<vid>[^,]+),(?P<hw_rev>[^:]+):(?P<serial>[^ format=""]+)"'
        
        # Regex Nomeada: Captura Interface, Valor de Potência e Status
        self.power_pattern = r'"(?P<interface>[^,]+),OPWR,(?P<value>[^,]+),dBm,(?P<status>[^"]+)"'

    def parse_inventory(self, file_path):
        results = []
        if not os.path.exists(file_path):
            print(f"⚠️ Arquivo não encontrado: {file_path}")
            return results
        
        with open(file_path, 'r') as f:
            content = f.read()
            for match in re.finditer(self.inventory_pattern, content):
                results.append(match.groupdict())
        return results

    def parse_power(self, file_path):
        results = []
        if not os.path.exists(file_path):
            return results
        
        with open(file_path, 'r') as f:
            content = f.read()
            for match in re.finditer(self.power_pattern, content):
                data = match.groupdict()
                data['value'] = float(data['value'])
                results.append(data)
        return results

class DatabaseManager:
    """Gerencia a conexão e persistência segura no PostgreSQL."""
    
    def __init__(self):
        # Busca credenciais das variáveis de ambiente (Segurança SecDevOps)
        self.conn_params = {
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASS"),
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", "5432")
        }

    def _connect(self):
        return psycopg2.connect(**self.conn_params)

    def save_inventory(self, data):
        query = """
            INSERT INTO optical_inventory (slot, model, vid, hw_rev, serial)
            VALUES (%(slot)s, %(model)s, %(vid)s, %(hw_rev)s, %(serial)s)
            ON CONFLICT (serial) DO UPDATE SET last_seen = CURRENT_TIMESTAMP;
        """
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    for row in data:
                        cur.execute(query, row)
            print(f"✅ {len(data)} placas sincronizadas no inventário.")
        except Exception as e:
            print(f"❌ Erro ao salvar inventário: {e}")

    def save_power_levels(self, data):
        query = """
            INSERT INTO optical_power (interface, power_value, status)
            VALUES (%(interface)s, %(value)s, %(status)s);
        """
        try:
            with self._connect() as conn:
                with conn.cursor() as cur:
                    for row in data:
                        cur.execute(query, row)
            print(f"✅ {len(data)} métricas de potência armazenadas.")
        except Exception as e:
            print(f"❌ Erro ao salvar potência: {e}")

def run_sentinel_checks(power_data):
    """Lógica de Inteligência: Thresholds de alarme crítico."""
    CRITICAL_THRESHOLD = -30.0
    alarms_found = 0
    
    print("\n🧐 Executando Sentinel Health-Check...")
    for entry in power_data:
        if entry['value'] <= CRITICAL_THRESHOLD:
            print(f"🚨 ALERTA CRÍTICO: Interface {entry['interface']} com sinal degradado! ({entry['value']} dBm)")
            alarms_found += 1
    
    if alarms_found == 0:
        print("🟢 Todos os níveis ópticos operando dentro da normalidade.")

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    inv_file = os.path.join(base_path, 'data', 'inventory_tl1.txt')
    pwr_file = os.path.join(base_path, 'data', 'optical_power_tl1.txt')

    parser = OpticalParser()
    db = DatabaseManager()

    print("🚀 Iniciando Optical-Sentinel Pipeline...")

    # Coleta e Parsing
    inventory = parser.parse_inventory(inv_file)
    power_metrics = parser.parse_power(pwr_file)

    # Persistência
    if inventory: db.save_inventory(inventory)
    if power_metrics: db.save_power_levels(power_metrics)

    # Inteligência do Sentinel
    run_sentinel_checks(power_metrics)

    print("\n🏁 Pipeline finalizado.")

if __name__ == "__main__":
    main()