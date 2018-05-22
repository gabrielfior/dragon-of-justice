import argparse
import datetime
from collections import namedtuple
from multiprocessing.dummy import Pool as ThreadPool

from typing import List

from corebot.requests_jarbas import Requester
from worker.MongoURM import Suspicious
from worker.congressperson import Congressperson


def get_suspicous_from_congressperson(congressperson : Congressperson):
    print('now :' + str(datetime.datetime.now()))

    # query jarbas for suspicous from this congressperson
    return Requester().find_suspicions(congressperson.applicant_id)


class MockMongo:

    def __init__(self):
        pass

    @staticmethod
    def get_seguindo_entries() -> List[Congressperson]:
        return [
            Congressperson(73441, 993,"CELSO RUSSOMANNO"),
            Congressperson(74010, 527,"VALDIR COLATTO"),
            Congressperson(160536, 2245,"MARCO TEBALDI")
        ]


def store_result_in_mongo(suspicious):
    #suspicousMongoObject = Suspicious(**suspicious)

    suspicousMongoObject = Suspicious(document_id = suspicious['document_id'],
        suspicious = suspicious['suspicions'],
        document_number = suspicious['document_number'],
        congressperson_id = suspicious['congressperson_id'],
        congressperson_name = suspicious['congressperson_name'],
        document_value = suspicious['document_value'],
        receipt=suspicious['receipt'],
        total_net_value = suspicious['total_net_value'],
        total_reimbursement_value = suspicious['total_reimbursement_value'],

        # FIXME - fix parsing problem
        #mongoengine.errors.ValidationError: ValidationError (Suspicious:6458176) (cannot parse date "2018-05-02T11:33:20.338995-03:00": ['last_update'])                                      #
        #last_update = suspicious['last_update'],
        #issue_date = suspicious['issue_date'],
        year = suspicious['year'],
        rosies_tweet = suspicious['rosies_tweet']
    )

    # TODO: define if suspicious should always be saved, or only if represents an update of previous saved version.
    # TODO: investigate if useful to use save_condition
    #https: // github.com / MongoEngine / mongoengine / blob / master / tests / document / instance.py
    print('Saving document_id {}'.format(suspicousMongoObject.document_id))
    suspicousMongoObject.save()


if __name__ == "__main__":

    # parse frequency (in minutes) to query mongo for suspicions
    parser = argparse.ArgumentParser(description='Corebot worker')
    parser.add_argument('-f', '--frequencyInMinutes', help='Frequency for querying Mongo for suspicous activitities',
                        required=True)

    args = vars(parser.parse_args())
    frequency = float(args['frequencyInMinutes'])

    # Get all 'seguindo' from mongo
    seguindo = MockMongo.get_seguindo_entries()

    # reference about threading in Python
    #http: // chriskiehl.com / article / parallelism - in -one - line /
    # Make the Pool of workers
    pool = ThreadPool(4)
    results = pool.map(get_suspicous_from_congressperson, seguindo)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()


    # results is a list of results for the congressmen.
    # store if do not exist in Mongo
    for j in results:
        for suspicious in j[0]:
            # now we have a suspicious
            store_result_in_mongo(suspicious)
    


    #schedule.every(frequency).minutes.do(run_threaded, job)
    #schedule.every(10).seconds.do(run_threaded, job)
    #schedule.every(10).seconds.do(run_threaded, job)

    #while 1:
    #    schedule.run_pending()
    #    time.sleep(1)


