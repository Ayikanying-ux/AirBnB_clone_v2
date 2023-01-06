#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            city_instance = []
            city_dict = models.storage.all(models.city.City)
            for k, v in city_dict.items():
                if v.state_id == self.id:
                    city_instances.append(v)
            return city_instance
