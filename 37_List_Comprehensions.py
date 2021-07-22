q = int(input())
w = int(input())
e = int(input())
n = int(input())
results = []
for x in range (q+1):  
    for y in range(w+1):
        for z in range (e+1):
            if x+y+z!=n:
                results.append([x,y,z])
print(results)