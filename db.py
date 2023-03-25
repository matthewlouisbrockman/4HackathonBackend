import uuid
from sqlalchemy import Column, Float, ForeignKey, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy.sql import func

Base = declarative_base()


class Games(Base):
    __tablename__ = 'games'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())


class Actions(Base):
    __tablename__ = 'actions'

    action_id = Column(String(36), primary_key=True, default=str(uuid.uuid4())) 
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    action = Column(String(500)) 
    actor = Column(String(100))

    game_id = Column(UUID(as_uuid=True), ForeignKey('game.id'))
    game = relation('Games')


class APICalls(Base):
    __tablename__ = 'apicalls'

    api_call_id = Column(String(36), primary_key=True, default=str(uuid.uuid4())) 
    provider = Column(String(50))
    model = Column(String(50))
    latency = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())
    cost = Column(Float, nullable=False)

    game_id = Column(UUID(as_uuid=True), ForeignKey('game.id'))
    game = relation('Games')


class Images(Base):
    __tablename__ = 'images'

    image_id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(TIMESTAMP, nullable=False, default=func.now())

    game_id = Column(UUID(as_uuid=True), ForeignKey('game.id'))
    game = relation('Games')
