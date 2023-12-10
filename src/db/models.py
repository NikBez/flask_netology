from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import func, String
from datetime import datetime


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class Advertisement(Base):
    __tablename__ = "advertisements"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    author: Mapped[str] = mapped_column(String(50), nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "author": self.author,
        }
