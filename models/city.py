#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='city')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

