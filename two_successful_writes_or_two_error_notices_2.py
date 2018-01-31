def write_both_successfully_or_leave_two_error_messages(msg):

    db1_client = DB1Client()
    db2_client = DB2Client()

    with leave_error_entries_on_any_failure(msg):
        db1_client.insert(msg)
        db2_client.insert(msg)


@contextmanager
def leave_error_entries_on_any_failure(msg):
    try:
        yield
    except (DB1InvalidMessage, DB2InvalidMessage):
        error_msg = make_error_message(msg)
        db1_client.upsert(error_msg)
        db2_client.upsert(error_msg)
