n= int(input())

a = list(map(int,input().split()))

maxn = a[0]
for i in range(n):
	if a[i] > maxn:
		maxn = a[i]

if maxn == a[0]:
	return 0

cnt = 0
cur = a[0]
while cur < maxn:
	cnt += 1
	cur *= 2

res = 0

while maxn > a[0]:
	maxn //= 2
	res += 1

return min(res, cnt)