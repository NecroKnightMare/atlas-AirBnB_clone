import json
import logging
import os

#from models.base_model import BaseModel#
#Configure logging (adjust as needed)#

logging.basicConfig(level=logging.INFO)


class FileStorage:
    """
    Handles serialization of objects to JSON file and deserialization of JSON file to objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.

        :return: Dictionary of all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        :param obj: Object to be added
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dicts = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dicts, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing).
        """
        DEBUG_MODE = True  # Set to False in production

        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dicts = json.load(f)
                for key, value in obj_dicts.items():
                    #class_name obj_id = key.split('.')
                    class_name = value['__class__']
                    obj = globals()class_name
                    self.__objects[key] = obj
                    if DEBUG_MODE:
                        print(f"Processing class: {class_name}")

                    try:
                        module = __import__('models.' + class_name, fromlist=[class_name])
                        class_ = getattr(module, class_name)
                        if DEBUG_MODE:
                            print(f"Successfully imported class: {class_name}")
                        FileStorage.__objects[key] = class_(**value)
                    except ImportError as e:
                        logging.error(f"Error importing class {class_name}: {str(e)}")
                    except AttributeError as e:
                        logging.error(f"Error getting class {class_name} from module: {str(e)}")
                    except Exception as e:
                        logging.error(f"Error creating instance of {class_name}: {str(e)}")
        except FileNotFoundError:
            logging.info(f"File '{FileStorage.__file_path}' not found. No objects loaded.")
        except Exception as e:
            logging.error(f"An error occurred during reload: {str(e)}")