# 46
class  Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		ans = []
		path = [0] * n  # []
		def dfs(i, s):
			if i == n:
				ans.append(path.copy())
				return
			for x in s:
				path[i] = x
				dfs(i + 1, s-{x})
		dfs(0, set(nums))
		return ans

'''
给你一个数字n，帮我输出所有的有效括号组合
比如：3
()()()
((()))
()(())
。。。'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # res = ''
        def dfs(i : int, leftpar: int, res: str) :
            if i == 2 * n and leftpar == n:
                ans.append(res)
                return 
            elif i == 2 * n: 
                return
            if leftpar < n and leftpar == i-leftpar:
                res+='('
                dfs(i + 1, leftpar + 1, res)
                res = res[:-1]
            elif leftpar < n and leftpar > i - leftpar:
                res+='('
                dfs(i + 1, leftpar + 1, res)  
                res = res[:-1]
                res+=')'
                dfs(i + 1, leftpar, res)
                res = res[:-1]
            elif leftpar >= n and leftpar > i - leftpar:
                res+=')'
                dfs(i + 1, leftpar, res)
                res = res[:-1]
        dfs(0, 0, '')
        return ans

  // 给你一个循环有序的数组，和一个target，帮我找到这个target在数组的位置。没有就返回-1
  // 没有重复元素，严格递增

 class Solution:
    def search(self, nums: List[int], target: int) -> int:
         
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[-1] and nums[mid] > target and target > nums[-1]:
                right = mid - 1
            elif nums[mid] > nums[-1]:
                left = mid + 1
            elif nums[mid] <= nums[-1] and nums[mid] < target and target <= nums[-1]:
                left = mid + 1
            elif nums[mid] <= nums[-1]:
                right = mid - 1
        return -1
// 假设有重复元素，要你找第一个出现的位置。你怎么优化？
    

    SELECT album_id, SUM(play_secs) AS total_play_secs
FROM userlog_play_secs
GROUP BY album_id
HAVING total_play_secs < (SELECT MAX(total_play_secs) FROM (SELECT album_id, SUM(play_secs) AS total_play_secs FROM userlog_play_secs GROUP BY album_id ORDER BY total_play_secs DESC LIMIT 1) AS top_album)
ORDER BY total_play_secs DESC
LIMIT 1;


# 2835
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if target > sum(nums):
            return -1
        ct = Counter(nums)
        ans = 0
        s = 0
        i = 0
        while 1 << i <= target:
            s += ct[1 << i] << i
            if s >= (target & ((1 << (i+1)) -1)):
                i+=1
                continue
            i += 1
            ans += 1
            while ct[1 << i] == 0 :
                i += 1
                ans += 1

        return ans
 
# 1483

# 2836
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        m = k.bit_length() - 1
        pa = [[(p, p)] + [None] *m  for p in receiver]
        for i in range(m):
        	for x in range(n):
        		p, s = pa[x][i]
        		pp, ss = pa[p][i]
        		pa[x][i + 1] = (pp, s + ss)
        ans =  0
        for i in range(n):
        	x = sum = i
        	for j in range(m +1):
        		if (k >> j) & 1 :
        			x, s = pa[x][j]
        			sum += s
        	ans = max(ans, sum)
        return ans

# 2815

# max pair sum in an array