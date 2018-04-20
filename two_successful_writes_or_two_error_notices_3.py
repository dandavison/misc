class DB1Client:
    def insert(self, msg):
        pass

    def upsert(msg):
        pass

class DB2Client:
    def insert(self, msg):
        pass

    def upsert(msg):
        pass

def write_both_successfully_or_leave_two_error_messages(msg):

    db1_client = DB1Client()
    db2_client = DB2Client()

    if is_valid(msg):
        db1_client.insert(msg)
        db2_client.insert(msg)


    try:
        db1_client.insert(msg)
        db2_client.insert(msg)
    except (DB1InvalidMessage, DB2InvalidMessage):
        db1_client.upsert(make_error_message(msg))
        db2_client.upsert(make_error_message(msg))
