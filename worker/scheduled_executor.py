import argparse
import datetime
from multiprocessing.dummy import Pool as ThreadPool

from typing import List

from worker.congressperson_enum import Congressperson


def get_suspicous_from_congressperson():
    print('now :' + str(datetime.datetime.now()))

def get_seguindo_entries(self) -> List:
    return [
        Congressperson(1, "VICENTINHO"),
        Congressperson(2, "MENDES"),
        Congressperson(3, "JARBAS")
    ]

if __name__ == "__main__":

    # parse frequency (in minutes) to query mongo for suspicions
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-f', '--frequencyInMinutes', help='Frequency for querying Mongo for suspicous activitities',
                        required=True)

    args = vars(parser.parse_args())
    frequency = float(args['frequencyInMinutes'])

    # Get all 'seguindo' from mongo
    seguindo = MockMongo().get_seguindo_entries()

    # Make the Pool of workers
    pool = ThreadPool(4)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(get_suspicous_from_congressperson, seguindo)
    # close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # reference about threading in Python
    #http: // chriskiehl.com / article / parallelism - in -one - line /

    #schedule.every(frequency).minutes.do(run_threaded, job)
    #schedule.every(10).seconds.do(run_threaded, job)
    #schedule.every(10).seconds.do(run_threaded, job)

    #while 1:
    #    schedule.run_pending()
    #    time.sleep(1)


