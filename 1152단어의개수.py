import itertools
row, max=[],[]

for i in range(9):
    a=list(map(int,input().split()))
    row.append(a)
    sort_a=sorted(a, reverse=True)   #행 숫자큰순서대로
    max.append(sort_a[0])  #각 행 최대값들
all=list(itertools.chain(*row))
max.sort(reverse=True)
ans=all.index(max[0])     #max[0]: 최댓값
r=ans//9+1
c=ans%9+1
print(max[0])
print(r,c)
