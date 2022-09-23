import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class EnvVariables(BaseSettings):

    es_host: str = os.getenv('ES_HOST')
    es_port: str = os.getenv('ES_PORT')
    vm_username: str = os.getenv('VM_USERNAME')
    vm_password: str = os.getenv('VM_PASSWORD')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    secret_key: str = os.getenv('SECRET_KEY')
    db_name:str = os.getenv('DB_NAME')
    db_user:str = os.getenv('DB_USER')
    db_pass:str = os.getenv('DB_PASS')
    db_host:str = os.getenv('DB_HOST')
    db_port:str = os.getenv('DB_PORT')

class Oids(BaseSettings):
    # OIDS Linux
    CPU_AVERAGE_1M = ".1.3.6.1.4.1.2021.10.1.3.1"
    CPU_AVERAGE_5M = ".1.3.6.1.4.1.2021.10.1.3.2"
    CPU_AVERAGE_15M = ".1.3.6.1.4.1.2021.10.1.3.3"
    CPU_NAME = ".1.3.6.1.2.1.25.3.2.1.3.196608"
    CPU_CORES = "iso.3.6.1.2.1.25.3.2.1.5" # Cada resultado devuelve 2 en mi caso porque tengo 2 CPU, y esos 4 resultados que devuelve son el numero de cores, es decir, 4
    NET_TRAFFIC_IN_1M = ".1.3.6.1.2.1.2.2.1.10.1"
    NET_TRAFFIC_IN_5M = ".1.3.6.1.2.1.2.2.1.10.2"
    NET_TRAFFIC_IN_15M = ".1.3.6.1.2.1.2.2.1.10.3"
    NET_TRAFFIC_OUT_1M = ".1.3.6.1.2.1.2.2.1.16.1"
    NET_TRAFFIC_OUT_5M = ".1.3.6.1.2.1.2.2.1.16.2"
    NET_TRAFFIC_OUT_15M = ".1.3.6.1.2.1.2.2.1.16.3"
    RAM_TOTAL = ".1.3.6.1.4.1.2021.4.5.0"
    RAM_USED = ".1.3.6.1.4.1.2021.4.6.0"
    RAM_FREE = ".1.3.6.1.4.1.2021.4.11.0"
    RAM_CACHED = "1.3.6.1.4.1.2021.4.15.0"
    
