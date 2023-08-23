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