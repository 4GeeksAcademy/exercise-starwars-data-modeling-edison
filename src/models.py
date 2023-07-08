import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float,DateTime, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Product(Base): 
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable= False)
    pricing = Column(Float, nullable = False)
    weight = Column(Float)
    color = Column(String(250), nullable= False)
    shopping_cart = Column(Integer, ForeignKey("shopping_cart"))


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable= False)
    last_name = Column(String(250), nullable= False)
    email = Column(String(250),nullable= False, unique=True)
    address = Column(String(250), nullable=False)
    shopping_cart = Column(Integer, ForeignKey("shopping_cart"))


class Bill(Base):
    __tablename__ = "bill"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    total_price = Column(Float, nullable= False)
    status = Column(String(30), Enum("paid","pending","refunded"))
    shopping_cart = Column(Integer, ForeignKey("shopping_cart"))


class shopping_cart(Base): 
    __tablename__ = "shopping_cart" 
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Float)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
