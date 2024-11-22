#!/usr/bin/env python3
""" Models Module
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    """Base Class"""
    pass

class User(Base):
    """User model class"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=False)
    session_id: Mapped[str] = mapped_column(String(250))
    reset_token: Mapped[str] = mapped_column(String(250))
