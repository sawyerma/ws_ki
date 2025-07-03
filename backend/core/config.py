import os
from dotenv import load_dotenv

# .env laden
load_dotenv()

class Settings:
    """
    Projektweite Settings für die Trading-API.
    """
    APP_TITLE = "Trading API"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = os.getenv("LOG_FORMAT", "%(asctime)s %(levelname)s %(message)s")

    # CORS
    CORS_ALLOW_ORIGINS = ["*"]
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]

    # Pfad zum Frontend (relative Angabe von hier: core/)
    FRONTEND_DIR = os.getenv(
        "FRONTEND_DIR",
        os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))
    )

    # ClickHouse-Verbindungsparameter
    CH_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")
    CH_PORT = int(os.getenv("CLICKHOUSE_PORT", "8123"))
    CH_DATABASE = os.getenv("CLICKHOUSE_DB", "bitget")
    CH_USER = os.getenv("CLICKHOUSE_USER", "default")
    CH_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "")

# Instanziiere globale Settings
settings = Settings()
