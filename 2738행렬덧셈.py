n, m=map(int,input().split())   #n: 줄 수, m: 원소개수
A, B=[],[]

for i in range(n):
    A.append(list(map(int,input().split())))
for j in range(n):
    B.append(list(map(int,input().split())))
for k in range(n):
    for l in range(m):
        print(A[k][l]+B[k][l], end=' ')
    print()