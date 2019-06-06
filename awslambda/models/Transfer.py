import json
from typing import Dict, Tuple


class Transfer:
    def __init__(self, data, *args, **kwargs):
        """Class for handling transfers

        Example:
        {
            created_datetime	Timestamp
            CreatedByUser	uid
            org	uid
            source	Connection
            source_mapping	DataMapping
            destination	Connection
            destination_mapping	DataMapping
            start_datetime	Timestamp
            frequency	
            OneTime	boolean
            RecordFilter	
            Name	string
            uid	uid
            active	boolean
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
        self._name = self.data.get("Name", None)
        self._created_date = self.data.get("created_datetime", None)
        self._created_by = self.data.get("created_by", None)
        self._organization = self.data.get("organization", None)
        self._source = self.data.get("source", None)
        self._source_mapping = self.data.get("source_mapping", None)
        self._destination = self.data.get("destination", None)
        self._destination_mapping = self.data.get("destination_mapping", None)
        self._start_date_time = self.data.get("start_datetime", None)
        self._frequency = self.data.get("frequency", None)
        self._record_filter = self.data.get("RecordFilter", None)
        self._active = self.data.get("active", True)

    def from_dict(self, transfer_dict: Dict):
        try:
            return transfer_dict
        except Exception as e:
            print("Parameter 'transfer_dict' is not a valid dict: " + e)

    def from_json(self, transfer_json: str):
        try:
            return self.from_dict(json.loads(transfer_json))
        except Exception as e:
            print("Parameter 'transfer_json' is not a valid JSON string: " + e)

    def from_tuple(self, transfer_tuple: Tuple):
        try:
            return {x[0]: x[1] for x in transfer_tuple}
        except Exception as e:
            print("Parameter 'transfer_tuple' is not valid: " + e)

    def to_dict(self):
        return self.data

    def to_json(self):
        return json.dumps(self.data)
