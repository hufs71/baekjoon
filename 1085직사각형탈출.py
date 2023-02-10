import math
x, y, w, h = map(int,input().split())

if (x>=w)&(y>=h):          #꼭지점 바깥
    print(math.sqrt((x-w)**2+(y-h)**2))
else:
    h1, w1 = abs(y-h), abs(x-w)       #w, h이랑 비교
    ans=[x, y, h1, w1]                #x, y축에 더 가까울 경우 in
    ans.sort()
    print(ans[0])