n, s = map(int, input().split())

w = []
v = []
for _ in range(n):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)

'''
def dfs(i, cur):
    if i < 0 or cur > s:
        return 0
    res = 0
    if w[i - 1] + cur <= s:
        res = max(dfs(i, cur + w[i-1]) + v[i-1],res)
    res = max(dfs(i - 1, cur), res)
    return res
     
print(dfs(n, 0))
'''


'''
def dfs(i, c):
    if i < 0:
        return 0
    if w[i] > c:
        return dfs(i - 1,c)
    return max(dfs(i - 1, c), dfs(i, c - w[i]) + v[i])
print(dfs(n - 1, s))
'''

f = [[0] * (s+ 1) for _ in range(n + 1)] 

for i, x in enumerate(w):
    for j in range(s + 1):
        if x > j:
            f[i+1][j] = f[i][j]
        else :
            f[i + 1][j] = max(f[i][j], f[i + 1][j - x] + v[i])
print(f[n][s])