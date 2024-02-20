#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade='all, delete', backref='place')
    else:
        @property
        def reviews(self):
            from models import storage
            reviews = []
            for k, v in storage.all():
                if k.partition['.'][0] == 'Review' and v.place_id == Place.id:
                    reviews.append(v)
            return (reviews)

    place_amenity = Table('place_amenity', metadata=Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False, cascade='all, delete', backref='place')
    else:
        @property
        def amenities(self):
            from models import storage
            amenities = []
            for amenity_id in amenity_ids:
                amenities.append(storage.all()[f'Amenity.{amenity_id}'])
            return (amenities)

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity:
                amenity_ids.append(obj.id)
