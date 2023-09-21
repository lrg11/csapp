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