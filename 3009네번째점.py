a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

for i in [a1, a2, a3]:
    if [a1, a2, a3].count(i)==1:
        a4=i
for i in [b1, b2, b3]:
    if [b1, b2, b3].count(i)==1:
        b4=i

print(a4,b4)