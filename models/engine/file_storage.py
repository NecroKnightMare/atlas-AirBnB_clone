import json
from models.base_model import BaseModel 


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Dictionary to store objects by `<class name>.id`.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        obj_dicts = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dicts, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the file exists,
        otherwise do nothing.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dicts = json.load(f)
                for key, value in obj_dicts.items():
                    class_name, obj_id = key.split('.')
                    FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
