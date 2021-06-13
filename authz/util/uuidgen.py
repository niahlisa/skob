from uuid import uuid4


def uuidgen():
    """
    generate new uuid for resources id field in database.
    """
    return uuid4().hex
