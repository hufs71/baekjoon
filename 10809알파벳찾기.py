T=int(input())
Rs=[]
Ss=[]
for i in range(T):
	R, S = input().split()
	Rs.append(int(R))
	Ss.append(S)

for i in range(T):
	for j in range(len(Ss[i])):
		print(Ss[i][j]*Rs[i], end='')
	print("")