#!/usr/bin/env python3
""" Models Module
"""
from flask import request
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    """User model class"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30), nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    session_id: Mapped[str] = mapped_column(nullable=True)
    reset_token: Mapped[str] = mapped_column(nullable=True)
