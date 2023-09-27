# IO
#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。


import sys
if __name__ == "__main__":
    # 读取第一行的n
    linx = input()
    n = int((linx.strip().split())[0])
    k = int((linx.strip().split())[1])
    ans = 0
    
    # 读取每一行
    line = input()
    # 或者 line = sys.stdin.readline()
 
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.strip().split()))
        
    #values.sort()
    def check(i: int) -> bool:
    	cnt = 1
    	pre = 0
    	j = 1
    	while j < len(values):
    		if values[j] - values[pre] >= i:
    			pre = j
    			j += 1
    			cnt += 1
    			if cnt >= k:
    				return True
    		else:
    			j += 1

    	return False

    if k == 2:
    	print(values[-1] - values[0])

    else:
    

	    right = values[-1] - values[0] + 1

	    left = 0

	    while left + 1 < right:
	    	mid = (left +right) // 2
	    	print("right: ", right)
	    	print("left:", left)
	    	if check(mid):
	    		left = mid
	    	else:
	    		right = mid
	    print(left)

# huawei
m, n = map(int, input().split())

gridlist = list(map(int, input().split()))

tx, ty = map(int, input().split())


grid = [[0] * n for _ in range(m)]

for i in range(m):
	grid[i] = gridlist[i*n: (i+1)*n]

sx = 0
sy = 0
v = 0
for i,x in enumerate(gridlist):
	if x > 0:
		v = x
		sx = i // n
		sy = i % n 
		break

q = [[sx, sy, v]]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
tag = 0
while q:
	if tag:
		break
	tmp = q
	for x, y, v in tmp:
		if x == tx and y = ty:
			print(v)
			tag = 1
			break
		for dx, dy in dir:
			if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and grid[x +dx][y + dy] == 0:
				grid[x +dx][y + dy]= v - 1
				q.append([x+dx, y+dy, v - 1])



n = int(input())

nums = list(map(int, input()))

sn = int(input())

start = end = 0

tag = False

start = nums.find(sn)
end = nums.rfind(sn)
if start == 0 and end == n - 1:
	for i, x in enumerate(nums):
		if x != sn:
			end = i - 1
			break
	for i in range(n - 2, -1, -1):
		if nums[i] != sn:
			start = i
			break

else :
	print(start, end)
'''
for i, x in enumerate(nums):
	if not tag and i == 0 and x == sn and nums[-1] != sn:
		tag = True
		start = i
	if tag and x != sn:
		end = i - 1
		tag = False
	if not tag and i != 0 and x ==
'''

k, n = map(int, input().split())

nodes = list(map(int, input().split()))

cnt = 1 

left = 0

def solve(node, shift):
    res = ""
    for i in range(len(node)):
        res += str(node[(i - shift) % len(node)])
    return res
    

ans = ""

while left < n:
    ans += solve(nodes[left:min(left + cnt , n)], k % (cnt if cnt != 0 else k))
    k *= 2
    left = left + cnt
    cnt = 2 * sum(i != -1 for i in nodes[left:left + cnt])
    
print(ans)

c = int(input())

while c:
    c -= 1
    n, m = map(int, input().split())
    ac = list(map(int, input().split()))
    bc = list(map(int, input().split()))
    sbc = set(bc)

    op = input().split(',')
    if op[0][0] == 'l':
        if op[1][0] == '=':
            ac.sort()
            ans = [[str(i),str(i)] if i in sbc else [str(i), 'null'] for i in ac ]
            print(len(ans))
            for a in ans:
                print(a[0], end= ' ')
                print(a[1])

import math
n, m = map(int,input().split())
a = []
b = []
tot = []
for _ in range(n):
    ai, bi = map(int,input().split())
    tot.append([ai, bi])
    a.append(ai)
    b.append(bi)

tot.sort()

vis = [False] * n
record = [[-1] * (m +1) for _  in range(n)]
def f(i, t):
    if i < 0 or t <= 0:
        return 0
    if record[i][t] != -1:
        return record[i][t]
    if vis[i]:
        record[i][t] =  max(f(i - 1, t), f(i, t - 1) + tot[i][1]) 
        return record[i][t]
    else:
        vis[i] = True
        #vis[i] = False
        record[i][t] = max(f(i, t - 1) + tot[i][0], f(i - 1, t))
        return record[i][t]
print(f(n - 1, m))
        

import math
n, m = map(int,input().split())

tot = []
for _ in range(n):
    ti = list(map(int,input().split()))
    tot.append(ti)



def dfs(i, ans):
    if i < 0:
        return max(ans)
    res = 100 * n
    for j in range(m):
        ans[j] += tot[i][j]
        res = min(res, max(dfs(i - 1, ans),ans[j]))
        ans[j] -= tot[i][j]
    return res

print(dfs(n - 1, [0] * m))

# meituan 3
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

# aliyun 2 
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