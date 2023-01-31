m=int(input())
n=int(input())
def so(n):   #약수확인
    ans=0
    if n==1:
        return 1
    else:
        for i in range(n):
            for j in range(n):
                if i*j==n:
                    ans+=1
        return ans       #약수개수
sum=0
s=[]

for i in range(m,n+1):
    if so(i)==0:
        sum+=i
        s.append(i)

if len(s)==0:
    print(-1)
else:
    print(sum)
    print(s[0])
