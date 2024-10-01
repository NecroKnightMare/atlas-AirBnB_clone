#!/usr/bin/python3
import json
import importlib


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
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
        obj_dicts = {key: obj.to_dict() for key, obj in
                     FileStorage.__objects.items()}
        
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(obj_dicts, f)
                print("Data written to file successfully")
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing).
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dicts = json.load(f)
                FileStorage.__objects.clear()
                for key, value in obj_dicts.items():
                    class_name, obj_id = key.split('.')

                    try:
                        # Modified dynamic import approach
                        module = __import__('models', fromlist=[class_name])
                        class_ = getattr(module, class_name)
                        instance = class_(**value)
                        self.new(instance)

                    except ImportError as e:
                        print(f"Error importing class {class_name}: {str(e)}") 
                    except AttributeError as e:
                        print(f"Error getting class {class_name} from module: {str(e)}")
                    except Exception as e:
                        print(f"Error creating instance of {class_name}: {str(e)}") 
        except FileNotFoundError:
            pass

    def destroy(self, obj):
        """Removes an object from __objects if it's present."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            print(f"Deleting object with key: {key}")
            del self.__objects[key]
            self.save()
