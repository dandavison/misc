class DB1Client:
    def insert(self, msg):
        pass

    def upsert(self, msg):
        pass


class DB2Client:
    def insert(self, msg):
        pass

    def upsert(self, msg):
        pass


def is_valid_message(msg):
    pass


def write_both_successfully_or_leave_two_error_messages(msg):

    db1_client = DB1Client()
    db2_client = DB2Client()

    try:
        if not is_valid_message(msg):
            raise InvalidMessage
        else:
            db1_client.insert(msg)
            db2_client.insert(msg)
    except Exception as exc:
        db1_client.upsert(format_as_error_message(msg))
        db2_client.upsert(format_as_error_message(msg))
        if not isinstance(exc, InvalidMessage):
            raise
