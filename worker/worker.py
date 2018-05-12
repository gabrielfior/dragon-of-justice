from typing import Dict

from corebot.db import MongoCore
from corebot.requests_jarbas import Requester
from worker.congressperson_enum import Congressperson


class Worker:

    def __init__(self):
        self.mongo_core = MongoCore()
        self.requester = Requester()

    def fetch_all_entries_congressperson(self) -> Dict :
        # query all entries from mongo's congressperson_collection
        # (congresspeople being followed)

        cursor = self.mongo_core.congressperson_collection.find()
        # TODO: loop cursor to get all entries and store into followed_people

        followed_people = [Congressperson({'id': 3059, 'name': "VICENTINHO JÚNIOR"})]

        for j in followed_people:
            # retrieve reimbursements
            self.requester.find_suspicions(j.ID)

            # TODO: store in mongo


