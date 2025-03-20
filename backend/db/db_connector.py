from sqlalchemy import Column, UUID
from sqlalchemy.orm import decl_base

Base = decl_base


class User(Base):
    __tablename__ = 'users'

    class Meta:
        id = Column(UUID(as_uuid=True), primary_key=True)