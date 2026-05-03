import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")
    AZURE_STORAGE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    AZURE_STORAGE_ACCOUNT_KEY = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
    AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "football-raw")
    SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
    SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
    SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
    SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE", "FOOTBALL_DB")
    SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH")
    SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA", "RAW")

    @classmethod
    def validate(cls):
        required = [
            "API_FOOTBALL_KEY",
            "AZURE_STORAGE_ACCOUNT_NAME",
            "AZURE_STORAGE_ACCOUNT_KEY",
            "SNOWFLAKE_ACCOUNT",
            "SNOWFLAKE_USER",
            "SNOWFLAKE_PASSWORD",
        ]
        
        missing = [item for item in required if not getattr(cls, item)]
        if missing:
            raise ValueError(f"missing required item(s): {missing}")