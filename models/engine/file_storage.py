import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file (e.g., 'file.json').
        __objects (dict): Dictionary to store objects by `<class name>.id`.
    """

    __file_path = "file.json"
    __objects = {}


