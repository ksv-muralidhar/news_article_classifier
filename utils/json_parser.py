import json


class JSONParser:
    """
    Parses json file whose path is provided as an input argument and returns a dict object.
    """
    def __init__(self, input_json_path: str):
        self.input_json_path = input_json_path  # path of json file to be parsed

    def parse_json(self):
        with open(self.input_json_path, 'r') as json_file:
            input_json = json.load(json_file)
        return input_json
