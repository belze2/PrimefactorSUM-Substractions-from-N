import matplotlib.pyplot as plt
import numpy as np
import pickle

with open('file.txt', 'rb') as file:
    # Load the pickled data
    data = pickle.load(file)

plt.plot(data.keys(), data.values(), marker='o')
plt.title('Down Scaling')
plt.xlabel('t')
plt.ylabel('N')
plt.show()
