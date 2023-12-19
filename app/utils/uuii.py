import uuid

class UniqueId():

    @classmethod
    def get_uuid(cls):
        return str(uuid.uuid4())