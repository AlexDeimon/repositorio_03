def print_rangoli(size):
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    return print('\n'.join(L[:0:-1]+L))
import string
alpha = string.ascii_lowercase
n=int(input())
print(print_rangoli(n))