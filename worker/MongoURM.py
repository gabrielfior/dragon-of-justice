import datetime
from mongoengine import *
connect('suspicions')

class Suspicious(Document):
    document_id = LongField(required=True, primary_key=True)
    suspicious = DictField(required=True)
    document_number = IntField(required=True)
    congressperson_id = LongField(required=True)

    # TODO - add as ReferenceField to seguindo collection
    congressperson_name = StringField(required=True)
    document_value = FloatField(required=True)

    receipt = DictField()
    total_net_value = FloatField()
    total_reimbursement_value = FloatField()
    last_update = DateTimeField(default=datetime.datetime.utcnow)
    issue_date = DateTimeField()
    year = IntField()
    rosies_tweet = StringField()

    # Initialize like this
    '''
    def __init__(self, **kwargs):
        self.document_id = kwargs.get('document_id')
        self.suspicions = kwargs.get('suspicions')

        
        document_number = kwargs.get()
        congressperson_id = kwargs.get()
        congressperson_name = kwargs.get()
        document_value = kwargs.get()

        receipt = kwargs.get()
        total_net_value = kwargs.get()
        total_reimbursement_value = kwargs.get()
        last_update = kwargs.get()
        issue_date = kwargs.get()
        year = kwargs.get()
        rosies_tweet = kwargs.get()
    '''
