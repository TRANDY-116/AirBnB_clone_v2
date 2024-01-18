#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a list of objects of one type of class"""

        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """sets in __objects with obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obg.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        serialized_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(serialized_objects, f)


    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                loaded_objects = json.load(f)
                for k, v in loaded_objects.items():
                    class_name = v['__class__']
                    obj = BaseModel(**v) if class_name == 'BaseModel' else globals()[class_name](**v)
                    self.__objects[k] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it's inside.

        Args:
            obj (BaseModel): The object to be deleted.

        Note:
            If obj is equal to None, the method does nothing.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
