from enum import Enum
from typing import Dict


class Congressperson(Enum):

    def __init__(self, mongo_entry: Dict):
        self.ID = mongo_entry['id']
        self.NAME = mongo_entry['name']
