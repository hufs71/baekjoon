a, b, c = list(map(int,input().split()))

if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)   #최초이익발생=손익분기+1
