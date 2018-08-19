import timeit
import time
import sys
import threading

def wrap_func(func, *args, **kwargs):
    """ Generator function to a single arg callable for timeit """
    def wrapped_func():
        return func(*args, **kwargs)
    return wrapped_func

def avg_time_func(func, number, *args, **kwargs):
    """ Times a given function and args 'number' of times, returns average.
        avg_time_func(func, number,[func args])
        
        func: the function to call without arguments
        number: the number of executions of func to time and get average of
        func args: the ordered and keyed arguments to give to func
    """
    wrapped = wrap_func(func, *args, **kwargs)
    total = timeit.timeit(wrapped, number=number)
    return total / number

def time_func(func, *args, **kwargs):
    """ Times a function with any given arguments given as args to this """
    return avg_time_func(func, 1, *args, **kwargs)

def human_readable_time_str(t):
    """ Returns a string that's easier to read when given a number 't'

        t: A number representing time
        Returns: a string with 's' for seconds prefixed by scientific prefixes
            i.e. 4.2*10**-8 = '4.2ns', 1234 = '20m33s'
    """
    if t < 60:
        fmt = lambda x, p: "{:.0f}{}".format(x, p)
        if (t * 10**9) < 10000: # use nano
            return fmt(t * 10**9, 'ns')
        elif (t * 10**6) < 10000: # use micro
            return fmt(t * 10**6, 'us')
        elif (t * 10**3) < 10000: # use milli
            return fmt(t * 10**3, 'ms')
        else:
            return fmt(t, 's')

    if t < 3600:
        m = int(t / 60)
        s = int(t) - (m * 60)
        return "{:d}m{:d}s".format(m, s)
    
    h = (t / 3600)
    m = (h - int(h)) * 60
    s = int((m - int(m)) * 60)
    h, m = int(h), int(m)
    return "{:d}h{:d}m{:d}s".format(h, m, s)

class Spinner:
    """ A stdout spinner run on a seperate thread.
        Usage:
            spinner = Spinner(delay=FLOAT_SEC)
            spinner.start()
            some_long_process()
            another_long_process()
            spinner.stop()
    """
    busy = False
    delay = 0.2

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield "[{}]".format(cursor)
    
    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay
    
    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.write('\b')
            sys.stdout.write('\b')
            sys.stdout.flush()
    
    def start(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()
    
    def stop(self):
        sys.stdout.write('\b')
        sys.stdout.write('\b')
        sys.stdout.write('\b')
        self.busy = False
        time.sleep(self.delay)