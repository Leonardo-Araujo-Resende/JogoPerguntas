import json


class ReadJSONFile:

    @staticmethod
    def read_json(json_file):
        return json.load(json_file)

