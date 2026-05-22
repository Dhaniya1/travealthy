from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from ..database import Base

class RouteSearch(Base):
    __tablename__ = "route_search"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True
    )

    source: Mapped[str] = mapped_column (
        String
    )

    destination: Mapped[str] = mapped_column(
        String
    )

    avg_aqi: Mapped[int] = mapped_column(
        Integer
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(datetime.timezone.utc)
    )