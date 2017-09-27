@periodic_task(bind=True, run_every=TIME_INTERVAL)
def process_items(task, chunk_size=CHUNK_SIZE):
    with advisory_lock('process_items', wait=False) as acquired:
        if not acquired:
            return

        items = db_query().order_by(something)[:chunk_size]

        if not items:
            raise Exception("All items processed")

        pool = ThreadPool(THREAD_POOL_SIZE)
        try:
            pool.map(process_item, items)
        finally:
            pool.close()
            pool.join()

        # Process the next chunk immediately, rather than waiting for the
        # periodic task to fire.
        task.delay()


def process_item(item):
    try:
        with transaction.atomic():
            _process_item(item)
    except Exception as ex:
        logger.exception("Error processing item %d" % item.id)
    finally:
        connection.close()
