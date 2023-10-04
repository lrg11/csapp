# 101

class Solution:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		return self.isSameTree(root.left, root.right)

# 110

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    	def f(root: Optional[TreeNode]) -> int:
    		if root == None:
    			return 0
    		left = f(root.left)
    		if left == -1:
    			return -1
    		right = f(root.right)
    		if right == -1 or abs(right-left) > 1:
    			return -1
    		return max(left, right) + 1

    	return f(root) != -1

# 199
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    	ans = []
    	def f(root: Optional[TreeNode], depth: int) -> None:
    		if root == None:
    			return

    		if depth == len(ans):
    			ans.append(root.val)

    		f(root.right, depth + 1)
    		f(root.left, depth + 1)
    	f(root, 0)
    	return ans
    	

# 849
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
    	res = 0
    	l = 0
    	size = len(seats)
    	while l < size and seats[l] == 0 :
    		l+= 1
    	res = max(res, l)
    	while l < size:
    		r = l + 1
    		while r < size and seats[r] == 0:
    			r += 1
    		if r == size:
    			res = max(res, r - l - 1)
    		else :
    			res = max(res, (r - l) // 2)
    		l = r
				
    	return res

# 513

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    	d = deque()
    	d.append(root)
    	# d = deque([root])
    	while d:
    		node = d.popleft()
    		if(node.right):
    			d.append(node.right)
    		if(node.left):
    			d.append(node.left)
    	return node.val

# 416 partition equal subset sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 :
            return False
        sm //= 2

        
        def dfs(i, c):
            if i < 0:
                return False if c else True
            if nums[i] > c:
                return dfs(i - 1, c)
            return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        return dfs(len(nums) - 1, sm)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 :
            return False
        sm //= 2

        n = len(nums)
        f = [[False] * (sm + 1) for _ in  range(n + 1)] 
        f[0][0] = True
        for i, x in enumerate(nums):
            for c in range(sm + 1):
                if x > c:
                    f[i + 1][c] = f[i][c] 
                else :
                    f[i + 1][c] = f[i][c] or  f[i][c - x] 
        return f[n][sm]
        
# 1262
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sm = sum(nums)
        if sm % 3 == 0:
            return sm 
        @cache
        def dfs(i, j):
            if i < 0:
                return -inf if j % 3 else 0
            return max(dfs(i - 1, j), nums[i] + dfs(i - 1, (j + nums[i]) % 3))
        return dfs(len(nums) - 1, 0)

# 823 
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        idx = {x: i for i, x in enumerate(arr)}
        @cache
        def dfs(j):
            res = 1
            for i in range(j):
                x = arr[i]
                v = arr[j]
                if v % x == 0 and v//x in idx:
                    res += dfs(i) * dfs(idx[v//x])
            return res
        return sum(dfs(x) for x in range(len(arr))) % (10** 9 + 7)


# 2571 minimum-operations-to-reduce-an-integer-to-0

class Solution:
    def minOperations(self, n: int) -> int:
        def dfs(i):
            if i & (i - 1) == 0:
                return 1
            low = i & (-i)
            return min(dfs(i + low), dfs(i - low)) + 1
        return dfs(n)