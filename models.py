from datetime import datetime
from typing import List
from db import db
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now)
    todos: Mapped[List["Todo"]] = relationship(back_populates="user")


class Todo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    description: Mapped[str] = mapped_column(
        String, unique=False, nullable=True)
    done: Mapped[bool] = mapped_column(
        Boolean, default=False, unique=False, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now)
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))
    user: Mapped["User"] = relationship(back_populates="todos")
