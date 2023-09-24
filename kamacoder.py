'''
k, n = map(int, input().split())

nodes = list(map(int, input().split()))

cnt = 1 

left = 0

def solve(node, shift):
    res = ""
    for i in range(len(node)):
        res += str(node[(i - shift) % len(node)])
        res +=" "
    print(res)
    return res

    

ans = ""
shift = 0
neg = 0
while left < n:
    ans += solve(nodes[left:min(left + cnt , n)], (2*shift - neg * 4 + k))
    shift = 2*shift + k
    tmp =  sum(i != -1 for i in nodes[left:left + cnt])
    neg = cnt - tmp
    left = left + cnt
    cnt = 2 * tmp
    
print(ans)

'''

k, n = map(int, input().split())
arr = list(map(int, input().split()))
 
idx = [0]
nxt = 0
cnt = 0
for i, num in enumerate(arr):
    if num != -1:
        cnt += 1
    if i == nxt:
        idx.append(nxt+1)
        nxt += cnt << 1
        cnt = 0
         
# idx = idx[:-1]
def reverse(i,j):
    j -= 1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
 
 
def shift(i,j,k):
    l = j - i
    k %= l
    reverse(i,j-k)
    reverse(j-k,j)
    reverse(i,j)
 
         
l = len(idx)
kk = k
for i in range(1, l):
    if i != l-1:
        for j in range(idx[i-1], idx[i]):
            if arr[j] != -1:
                pre = arr[j]
                break
    shift(idx[i-1],idx[i],kk)
    if i != l -1:
        cnt = 0
        for j in range(idx[i-1], idx[i]):
            if arr[j] == pre:
                break
            elif arr[j] != -1:
                cnt += 1
        kk = k + 2*cnt
print(' '.join(map(str,arr)))