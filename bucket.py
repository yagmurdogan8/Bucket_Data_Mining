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

# storing bucket function's result into 'result' variable
result = bucket(n, N)

# plot of result with labels and axis grids
plt.hist(result, bins = range(1, n), rwidth = 0.5) # plotting the graph with 0.5 spaces between
plt.xlabel('Number of the Distinct Values') # label of axis x
plt.ylabel('Frequency') # label of axis y
plt.title(f'Distribution of Distinct Values for {n} Random Integers & {N} Buckets') # title of the graph
plt.grid(axis = 'both') # dividing into both x and y axis grids
plt.show() # show the graph