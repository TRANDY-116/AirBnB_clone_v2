#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models  # assuming 'models' module is imported


class State(BaseModel, Base):
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # For DBStorage
    if models.storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')

    # For FileStorage
    else:
        @property
        def cities(self):
            city_list = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
