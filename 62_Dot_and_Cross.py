import numpy as np
N=int(input())
a = np.array([input().split() for _ in range(N)],int)
b = np.array([input().split() for _ in range(N)],int)
c = np.dot(a,b)
print (c)