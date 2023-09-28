a = input()

a+='#'

n = len(a)
cnt = 1
res = 0
t = []
for i in range(1,n):
	if a[i - 1] == a[i]:
		cnt += 1
	else:
		res += cnt - min(2, cnt)
		t.append(min(2, cnt))
		cnt = 1
#res += cnt - min(2, cnt)
#t.append(min(2, cnt))

for i in range(2, len(t)):
	if t[i - 1] == 2 and t[i - 2] == 2:
		res += 1
		t[i - 1] -= 1

print(res)

