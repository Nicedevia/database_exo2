from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(88), nullable=False)
    last_name = Column(String(88), nullable=False)
    email = Column(String(320), nullable=False, unique=True)

    products = relationship("Product", back_populates="user", uselist=False, cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_customer = Column(String(80), nullable=False)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    user = relationship("User", back_populates="orders")

    def __init__(self, name_customer, quantity, user):
        self.name_customer = name_customer
        self.quantity = quantity
        self.user = user

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    price = Column(Float(precision=8), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="products")
