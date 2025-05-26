from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from fast_zero.settings import Settings

engine = create_engine(
    Settings().DATABASE_URL,
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)


# pragma: no cover
def get_session():
    with Session(engine) as session:
        yield session
