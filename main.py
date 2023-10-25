from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from components.info import get_orders_with_product_info
from models.model import Base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATABASE_HOST = "localhost"
DATABASE_NAME = "my_database_appli"
DATABASE_USERNAME = "root"
DATABASE_PASSWORD = "root"

engine = create_engine(f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}")

Session = sessionmaker(bind=engine)
get_orders_with_product_info(Session())

Base.metadata.create_all(engine)
