from database import db
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from datetime import datetime

# Table: allowed_machines
class AllowedMachine(db.Model):
    __tablename__ = 'allowed_machines'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(255), nullable=False)
    mac = Column(String(255), nullable=False)
    tool_name = Column(String(255), nullable=False)
    expiry_date = Column(DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('mac', 'tool_name', name='unique_mac_tool'),
    )

# Table: pending_machines
class PendingMachine(db.Model):
    __tablename__ = 'pending_machines'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(255), nullable=False)
    mac = Column(String(255), nullable=False)
    tool_name = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint('mac', 'tool_name', name='pending_unique_mac_tool'),
    )
