class DB1Client:
    def insert(self, msg):
        pass

    def upsert(self, msg):
        if exists_in_db(get_primary_key(msg)):
            self.update(msg)
        else:
            self.insert(msg)


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

    if not is_valid_message(msg):
        db1_client.insert(format_as_error_message(msg))
        db2_client.insert(format_as_error_message(msg))
    else:
        try:
            db1_client.insert(msg)
            db2_client.insert(msg)
        except:
            db1_client.upsert(format_as_error_message(msg))
            db2_client.upsert(format_as_error_message(msg))
            raise

