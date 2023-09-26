import random # to generate random numbers
import matplotlib.pyplot as plt # to sketch the graph

# Changeable test numbers
n = 750 # number of coins to throw
N = 500 # number of empty buckets

# defining a function to store distinct number's count for the random n and N values
def bucket(n, N):
    distinct_num_counts = [] # distinct number count
    for i in range(n):
        distinct_set = set()
        for j in range(n):
            rand_int = random.randint(1, N)
            distinct_set.add(rand_int)
        distinct_num_counts.append(len(distinct_set))
    return distinct_num_counts