if False:
    done_trade_this_tick = False
    trade_lock = Lock()


    def _fetch_all_and_trade():
        def _fetch_and_maybe_trade():
            http_fetch()
            with trade_lock:
                if
                trade()

        thread_pool = ThreadPool()
        thread_pool.map(_fetch_and_maybe_trade, markets)
        thread_pool.close()
        thread_pool.join()

    thread = threading.Thread()
    thread.run(_fetch_all_and_trade)
