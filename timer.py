# Purpose: Timer class for timing code execution
import time
import sys


class Timer:
    """
    Usage:
        with Timer("my_function"):
            my_function()

        With Timer("my_function", verbose=True):
            my_function()

        T = Timer("my_function")
        t.start()
        my_function()
        t.stop()

        T = Timer("my_function", verbose=True)
        t.start()
        my_function()
        t.stop()
    """

    def __init__(self, name, verbose=False):
        self.name = name
        self.verbose = verbose
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def __enter__(self):
        self.start()

    def __exit__(self, type, value, traceback):
        self.stop()

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if self.verbose:
            print(f"\n 👁️ 🫦 👁️  {self.name} elapsed time: {self.elapsed_time:.4f} seconds  👁️ 🫦 👁️ \n")
        else:
            print(f"You silly forgot to set verbose=True! 🤠🤠🤠🤠🤠")


if __name__ == "__main__":
    try:
        with Timer("Programming challenge", verbose=True):
            time.sleep(10e6)
    except KeyboardInterrupt:
        sys.exit(0)  # or 1, or whatever

