n = int(input())
lista = list(map(int, input().split()))

def so(n):
    ans=0
    if n==1:
        return 1
    else:
        for i in range(n):
            for j in range(n):
                if i*j==n:
                    ans+=1
        return ans
count=0
for i in range(n):
    if so(lista[i])==0:
        count+=1
print(count)