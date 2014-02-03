# quick script to pickle a list of all fibonaci sequence numbers
import math

def nth_fib(n):
    return int((((1+math.sqrt(5.0))/2.0)**n)/math.sqrt(5.0)+0.5)


def fibs_to_file(limit):
    data = []
    for i in range(1,limit):
        data.append((i, str(nth_fib(i))))
    return data

fibs_list = fibs_to_file(1475)
import pickle
pickle.dump(fibs_list, open('fibs_list.pkl', 'wb'))
