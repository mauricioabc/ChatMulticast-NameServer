from sqlalchemy import Column, String, Integer
from DatabaseManager import Base
from sqlalchemy import Column, Integer, DateTime
from typing import Any


class ChatMulticastInfo(Base):
    __tablename__ = 'ChatMulticastInfo'

    Id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    IpAddress = Column(String(100), nullable=False)  # NOT NULL
    Port = Column(Integer, nullable=False)  # NULL
    ChatCryptoKey = Column(String(2048), nullable=True)
    InsertDate = Column(DateTime, nullable=False)

    def __init__(self, Name, IpAddress, Port, InsertDate, ChatCryptoKey=None):
        self.Name = Name
        self.IpAddress = IpAddress
        self.Port = Port
        self.ChatCryptoKey = ChatCryptoKey
        self.InsertDate = InsertDate

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()
