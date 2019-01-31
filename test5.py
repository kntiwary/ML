# https://www.notion.so/Lock-7d46e280db894aa9bfd00c98c2adb1de

import os
import sys
from threading import Thread,Lock




class Locker(object):
    def __init__(self):
        self.lock = Lock()
        self.count=0

    def increment(self, offset):
        with self.lock:
          self.count += offset





def worker(sensor_index, count_per_thread, counter):
    for _ in range(count_per_thread):
        counter.increment(1)


def run_threads(func, num_of_threads, count_per_thread, counter):
    threads = []
    for i in range(num_of_threads):
        args = (i, count_per_thread, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def print_usage():
    print("Usage:- python {} num_of_threads count_per_thread".format(
        os.path.basename(__file__),
    ))


def parse_arg():
    try:
        return int(sys.argv[1]), int(sys.argv[2])
    except ValueError:
        print_usage()
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        num_of_threads, count_per_thread = parse_arg()
        # counter = Counter()
        counter = Locker()
        run_threads(worker, num_of_threads, count_per_thread, counter)
        print('Counter should be %d, found %d' % (
            num_of_threads * count_per_thread, counter.count,
        ))
    else:
        print_usage()
        exit(1)