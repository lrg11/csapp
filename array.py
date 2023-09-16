#2531
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        for l, c in c1.items():
            for r, d in c2.items():
                if l == r and len(c1) == len(c2):
                    return True 
                elif l!= r and  len(c1) - (c1[l]== 1) + (not (r in c1)) == len(c2) - (c2[r]== 1) + (not (l in c2)):
                    return True
                
        return False
            

#2531
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        for l, c in c1.items():
            for r, d in c2.items():
                if l == r:
                    if len(c1) == len(c2):
                        return True 
                elif len(c1) - (c == 1) + ((r not in c1)) == len(c2) - (d== 1) + ((l not in c2)):
                    return True
                
        return False
            

# 2497

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        neighb = [[] for _ in vals]
        for edge in edges:
            if vals[edge[0]] > 0:
                neighb[edge[1]].append(vals[edge[0]])
            if vals[edge[1]] > 0:
                neighb[edge[0]].append(vals[edge[1]])
        ans = -inf
        for v, nb in zip(vals, neighb):
            ans = max(ans, v + sum(nlargest(k, nb)))
        return ans

# 210

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for x, y in prerequisites:
            indeg[x] += 1
            g[y].append(x)
        dq = deque()
        ans = []
        for i,x in enumerate(indeg):
            if x == 0:
                dq.append(i)
                ans.append(i)
        while dq:
            tmp = dq.popleft()
            for n in g[tmp]:
                indeg[n]-= 1
                if indeg[n] == 0:
                    dq.append(n)
                    ans.append(n)
        return ans if len(ans) == numCourses else []


#2482
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onesRow = [0] * m
        onesCol = [0] * n
        for i, cols in enumerate(grid):
            for col in cols:
                if col == 1: 
                    onesRow[i] += 1
            print(onesRow[i])
        for j, rows in enumerate(zip(*grid)):
            for row in rows:
                if row == 1: 
                    onesCol[j] += 1
            print(onesCol[j])
        ans = []
        for i in range(m):
            res = []
            for j in range(n):
                res.append(2* onesRow[i] + 2*onesCol[j] - m - n)
            ans.append(res)
        return ans


# 2483

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        d = [0]  * (n + 1)
        for i in range(n-1, -1, -1):
            d[i] = d[i + 1] + (customers[i] == 'Y')

        res = [n + 1] * (n+1)
        precost = 0
        for i in range(n + 1):
            
            cost = precost + d[i]
            if res[cost] == n + 1:
                res[cost] = i
            if i < n:
                precost += (customers[i] == 'N')
            
        for num in res:
            if num != n + 1:
                return num
        return -1
## !!! TLM

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_cost = cost = customers.count('Y')
        ans = 0

        for i, c in enumerate(customers):
            if c == 'N':
                cost += 1
            else:
                cost -= 1
                if cost < min_cost:
                    min_cost = cost
                    ans = i + 1
            
        return ans

# 2484

class Solution:
    def countPalindromes(self, s: str) -> int:
        suf = [0] * 10
        suf2 = [0] * 100

        for v in map(int, reversed(s)):
            for j in range(10):
                suf2[j +v * 10] += suf[j]
            suf[v]+= 1

        ans = 0
        pre = [0]*10
        pre2= [0]  * 100
        for v in map(int, s):
            suf[v] -= 1;
            for j in range(10):
                suf2[j +v * 10] -= suf[j]
            ans += sum(c1* c2 for c1, c2 in zip(pre2, suf2))
            for j in range(10):
                pre2[j +v * 10] += pre[j]
            pre[v]+= 1
        return ans % (10**9 + 7)

#2498
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = stones[1] - stones[0]
        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i - 2])
        #for i in range(1, len(stones) - 2):
         #   ans = max(ans, stones[i+2] - stones[i])
        return ans

#2366
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        m = nums[-1]
        ans = 0
        n = len(nums)
        for i in range(n - 2, -1, -1):
            num = nums[i]
            k = (num - 1) // m
            ans += k
            m = num // (k + 1)
        return ans

# 2364

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n * (n - 1) // 2
        cnt = Counter()
        for i, x in enumerate(nums):
            ans -= cnt[i - x]
            cnt[i - x]+=1
        return ans

# 2363

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = Counter(dict(items1))
        cnt += dict(items2)
        return sorted(cnt.items())

# 2848
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)
        for start, end in nums:
            diff[start] += 1
            diff[end + 1] -= 1
        return sum(s > 0 for s in accumulate(diff))

# 300

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i: int) -> int:
        
            res = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j) + 1)
            return res

        return max(dfs(i) for i in range(n))
            
# 2739
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        #return int(10 * (min(mainTank // 5, additionalTank) + mainTank))
        ans = 0
        while mainTank >= 5:
            ans += 5
            mainTank -= 5
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1

        return (ans + mainTank) * 10 

# 2740
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(1, n):
            if nums[i] - nums[i - 1] < ans:
                ans = nums[i] - nums[i - 1]
        return ans


# 46
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        ans = []
    
        def dfs(i: int) ->None:
            if i == 0:
                ans.append(arr.copy())
                return
            for j in range(n):
                if (i >> j) & 1:
                    arr.append(nums[j])
                    dfs(i ^ (1 << j))
                    arr.pop()
        dfs((1 << n) - 1)
        return ans

# 2741
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        ans = 0
        MOD = 10** 9 +7
        n = len(nums)

        @cache
        def dfs(i: int, k:int) -> int:
            if i == 0:
                return 1
            res = 0
            for j in range(n):
                if (i >> j) & 1 and (nums[j] % nums[k] == 0 or nums[k] % nums[j] == 0):
                    res +=   dfs(i ^ (1 << j), j)
            return res
        return sum(dfs(((1 << n) - 1) ^(1 << i), i) for i in range(n)) % MOD 

# 2643

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,-inf]
        for j, row in enumerate(mat):
            if sum(i == 1 for i in row) > ans[1]:
                ans[1] = sum(i == 1 for i in row)
                ans[0] = j

        return ans

# 2644

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxd = -inf
        ans = 0
        for d in divisors:
            if sum(n % d == 0 for n in nums) > maxd:
                maxd = sum(n % d == 0 for n in nums)
                ans = d
            elif sum(n % d == 0 for n in nums) == maxd and d < ans:
                ans = d

        return ans