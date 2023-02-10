import math
test = int(input())
ans=[]      #진입/이탈
while test!=0:
    count=0        #진입/이탈 수
    x1, y1, x2, y2 = map(int, input().split())   #출발, 도착
    n = int(input())   #행성계 개수
    for i in range(n):
        cx, cy, r = map(int, input().split()) #행성계 중점, 반지름
        if (math.sqrt((x1-cx)**2+(y1-cy)**2)<r) & (math.sqrt((x2-cx)**2+(y2-cy)**2)<r):  #출발, 도착 둘 다 행성계 안
            continue
        elif math.sqrt((x1-cx)**2+(y1-cy)**2)<r:    #출발만 행성계 안
            count+=1
        elif math.sqrt((x2-cx)**2+(y2-cy)**2)<r:  # 하나만 행성계 안
            count+=1
        else:
            continue    #출발, 도착 둘 다 행성계 밖
    ans.append(count)

    test-=1

for i in ans:
    print(i, end= '\n')