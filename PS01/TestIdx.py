import numpy as np

a = np.arange(10)

for i in range(len(a),0,-1):
    j = len(a)-i
    k = j + 3
    print(i," -- ", a[j:k])
