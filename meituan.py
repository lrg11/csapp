'''
n = int(input())

num = []
for i in range(n):
    a = list(map(int, input().split()))
    num.append(list(set(a)))

base = n*(n - 1) // 2

ans = []
def qw(start, tack):
    if len(tack) == 2:
        ans.append(tack.copy())
        return
    for i in range(start, n):
        tack.append(i)
        qw(i + 1, tack)
        tack.pop()

qw(0, [])
cnt = 0

print(len(ans))
for [i, j]  in ans:
    print(i,j)
    cnt += len(set(num[i]).union(set(num[j])))
print(cnt / base)
'''

from collections import defaultdict


n = int(input())

num = []
for i in range(n):
    a = list(map(int, input().split()))
    a = a[1:]
    num.append(list(set(a)))

base = n*(n - 1) // 2

cnt = 0

mp = defaultdict(int)
for nu in num:
    cnt += len(nu) * (n - 1)
    for c in nu:
        mp[c]+= 1

for v in mp.values():
    cnt -= v * (v - 1) // 2

'''
for k, v in mp.items():
    cnt -= v * (v - 1) // 2
'''
print(cnt / base)

'''
my_dict = {'a': 1, 'b': 2, 'c': 3}  
  
for [key, value] in my_dict.items():  
    print("Key:", key)  
    print("Value:", value)
'''