#!/usr/bin/env python3


def realize_event_states(event_sequences):
    path2savepoint = {}
    for event_sequence in event_sequences:
        path = ()
        for event in event_sequence:
            path += event,
            try:
                savepoint = path2savepoint[path]
            except KeyError:
                event()
                path2savepoint[path] = transaction.savepoint()
                yield
            else:
                transaction.savepoint_rollback(savepoint)


def test():
    for event_sequence in realize_event_states(get_event_sequences()):
        for event in event_sequence:
            test_assertions()
