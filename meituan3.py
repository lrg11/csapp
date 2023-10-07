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



# 

n = int(input())

num = []
for i in range(n):
    a = list(map(int, input().split()))
    num.append(list(set(a)))

base = n*(n - 1) // 2

ans = []
def qw(start, tack):
    if len(tack) == 2:
        ans.append(tack)
    for i in range(start, n):
        tack.append(i)
        qw(start + 1, tack)
        tack = tack[:-1]

qw(0, [])
cnt = 0

for [i, j]  in ans:
    print(i,j)
    cnt += len(set(num[i]).union(set(num[j])))
print(cnt / base)


# 

from functools import cache

import sys

try:
    while True:
        line = sys.stdin.readline().strip()
        
        n = len(line)
        if n < 3:
            print(0)
            break
        cnt = 0
        for i in range(n):
            if cnt == 0 and line[i] == "m":
                cnt += 1
            if cnt == 1 and line[i] == "e":
                cnt += 1
            if cnt == 2 and line[i] == "i":
                cnt += 1
        if cnt < 3:
            print(0)
            break
   
        @cache
        def delstr(deln, used):
            used = list(used)
            if deln == 0:
                newline = ""
                for i in range(n):
                    if used[i] == 0:
                        newline += line[i]
                if "mei" in newline:
                    return 1
                return 0
            ans = 0
            for i in range(n):
                if used[i]!= 0:
                    continue
                if i == 0:
                    if used[i + 1] == 0:
                        used[i] = 1
                        ans += delstr(deln - 1, tuple(used))
                        used[i] = 0
                elif i == n - 1:
                    if used[i - 1] == 0:
                        used[i] = 1
                        ans += delstr(deln - 1, tuple(used))
                        used[i] = 0
                else:
                    if used[i - 1] == 0 and used[i + 1] == 0:
                        used[i] = 1
                        ans += delstr(deln - 1, tuple(used))
                        used[i] = 0

            return ans
        ans = 0
        for i in range(n - 3 + 1):
            ans += delstr(i, tuple([0] * n))

        print(ans)
        break
            
            


        
except:
    pass

#  
import sys

try:
    while True:
        line = sys.stdin.readline().strip()
        
        n = len(line)
        if n < 3:
            print(0)
            break
        cnt = 0
        for i in range(n):
            if cnt == 0 and line[i] == "m":
                cnt += 1
            if cnt == 1 and line[i] == "e":
                cnt += 1
            if cnt == 2 and line[i] == "i":
                cnt += 1
        if cnt < 3:
            print(0)
            break
   
       
        def delstr(deln, used):
            used = list(used)
            if deln == 0:
                newline = ""
                for i in range(n):
                    if used[i] == 0:
                        newline += line[i]
                if "mei" in newline:
                    return 1
                return 0
            ans = 0
            for i in range(n):
                if used[i]!= 0:
                    continue
                if i == 0:
                    if used[i + 1] == 0:
                        used[i] = 1
                        ans += delstr(deln - 1, used)
                        used[i] = 0
                elif i == n - 1:
                    if used[i - 1] == 0:
                        used[i] = 1
                        ans += delstr(deln - 1, used)
                        used[i] = 0
                else:
                    if used[i - 1] == 0 and used[i + 1] == 0:
                        used[i] = 1
                        ans += delstr(deln - 1, used)
                        used[i] = 0

            return ans
        ans = 0
        for i in range(n - 3 + 1):
            ans += delstr(i, tuple([0] * n))

        print(ans)
        break
            
            


        
except:
    pass