from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings
from src.db.models import Base


class DBConnnector:
    def __init__(self, url, echo=False):
        self.db_url = url
        self.engine = create_engine(self.db_url, pool_pre_ping=True, echo=echo)
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def __enter__(self):
        self.session = self.session_factory()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def init_models(self):
        with self.engine.begin() as conn:
            Base.metadata.create_all(bind=conn)


connection = DBConnnector(settings.db_url)
