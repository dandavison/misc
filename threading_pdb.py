from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import ipdb as pdb
import requests
from time import sleep


def task():
    print('In task')
    while True:
        a_variable = 1
        print(requests.get('http://theguardian.com'))
        pdb.set_trace()
        sleep(1)
    return


if __name__ == '__main__':
    # ipdb complains if not called in the main thread
    pdb.set_trace()

    thread = Thread(target=task)
    print('Starting `threading` thread')
    thread.start()
    thread.join()

    with ThreadPoolExecutor(max_workers=1) as executor:
        print('Starting `concurrent.futures` thread')
        future = executor.submit(task)
        print(future.result())

    print('Done')
