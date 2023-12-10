from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


load_dotenv()
db_name = os.getenv("MYSQL_DB_NAME", "test.db")


@dataclass
class Settings:
    db_url: str = "sqlite:///" + str(
        Path(__file__).resolve().parent.parent.joinpath(db_name)
    )


settings = Settings()
