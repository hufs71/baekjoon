import sys
import time
start=time.time()
def a(n):
    f = [0,1,2]
    if n>=3:
        for i in range(3, n+1):
            f.append((f[i-1]+f[i-2])%15746)
    return f[n]
n = int(sys.stdin.readline())
print(a(n))
end=time.time()
print(f'\n{end-start:.5f}sec')
