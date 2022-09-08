import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

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