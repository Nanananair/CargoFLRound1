from email.mime import base
from typing import Text
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy.sql.sqltypes import Boolean

base = declarative_base()

class Employee(base): 
    __tablename__ = 'employees'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String,nullable=False)
    mobile_no = Column(String(20), nullable=False)
    email = Column(String, unique=True, nullable=False)
    employee_branch = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_on =  Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, name, mobile_no, email, employee_branch  ) -> None:
        super().__init__()
        self.name = name
        self.mobile_no = mobile_no
        self.email = email
        self.employee_branch = employee_branch

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}