from database.db import Base, engine
from database.models import Order


Base.metadata.create_all(bind=engine)