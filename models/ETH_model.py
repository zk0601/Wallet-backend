from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, DECIMAL
from datetime import datetime

Base = declarative_base()


class EthBalance(Base):
    __tablename__ = 'ETH'

    id = Column(Integer, primary_key = True, autoincrement=True)
    platform = Column(String(64), nullable=False)
    time = Column(DateTime, nullable=False)
    balance = Column(DECIMAL(16, 4), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class EthTrade(Base):
    __tablename__ = 'ETH_trade'

    id = Column(Integer, primary_key=True, autoincrement=True)
    platform = Column(String(64), nullable=False)
    platform_address = Column(String(255), nullable=False)
    trade_time = Column(DateTime, nullable=False)
    from_address = Column(String(255), nullable=False)
    to_address = Column(String(255), nullable=False)
    value = Column(DECIMAL(16, 4), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
