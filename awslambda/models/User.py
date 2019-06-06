import json
from typing import Dict, Tuple


class User:
    def __init__(self, data, *args, **kwargs):
        """Class for handling Users

        Example:
        {	
            "uid": uid
            "org": uid
            "created_datetime": Timestamp
            "Roles": Array[string]
        }

        """
        if isinstance(data, dict):
            self.data = self.from_dict(data)
        elif isinstance(data, str):
            self.data = self.from_json(data)
        elif isinstance(data, tuple):
            self.data = self.from_tuple(data)
        else:
            raise AssertionError(
                "Parameter 'data' was not a valid input: dict, tuple, or JSON string"
            )

        self._uid = self.data.get("uid", None)
        self._name = self.data.get("Name", [])
        self._created_date = self.data.get("created_datetime", None)
        self._organization = self.data.get("organization", None)

    def from_dict(self, user_dict: Dict):
        try:
            return user_dict
        except Exception as e:
            print("Parameter 'user_dict' is not a valid dict: " + e)

    def from_json(self, user_json: str):
        try:
            return self.from_dict(json.loads(user_json))
        except Exception as e:
            print("Parameter 'user_json' is not a valid JSON string: " + e)

    def from_tuple(self, user_tuple: Tuple):
        try:
            return {x[0]: x[1] for x in user_tuple}
        except Exception as e:
            print("Parameter 'transfer_tuple' is not valid: " + e)

    def to_dict(self):
        return self.data

    def to_json(self):
        return json.dumps(self.data)
