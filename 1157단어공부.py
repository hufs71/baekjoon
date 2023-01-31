word=input().lower()
s='abcdefghijklmnopqrstuvwxyz'
num=[]
for i in s:
    num.append(word.count(i))
num2=sorted(num,reverse=True)
if num2[0]==num2[1]:         #num[0]: 가장 많은 알파벳 개수
    print('?')
else:
    print(s[num.index(num2[0])].upper())