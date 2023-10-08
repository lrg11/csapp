#238 product of array except self 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product0 = 1
        cnt  = 0
        for n in nums:
            product *= n
            if n != 0:
                product0*= n
            else:
                cnt += 1
    
        ans = [0] * len(nums)
        
        for i,x  in enumerate(nums):
            if x != 0:

                
                product  //= x
                ans[i] = product
                product *= x
            else:
                ans[i] =  0 if cnt > 1 else product0
        return ans
# better

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        
        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1;
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i]
        
        return answer


# longest substring without repeating

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        left = 0
        right = 0
        ans = 0
        for i,x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]]-= 1
                left+= 1
            ans = max(ans, i - left + 1)
        return ans

# 128 longest consecutive sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        ans = 0
        for n in nset:
            if n - 1 not in nset:
                cur = n
                cnt = 1
                while cur + 1 in nset:
                    cur += 1
                    cnt += 1
                ans = max(cnt, ans)
        return ans

# 57 insert interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        left = newInterval[0]
        right = newInterval[1]
        placed = False
        for x, y in intervals:
            if left > y:
                
                ans.append([x,y])

            elif right < x:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([x, y])
            else:
                left = min(left, x)
                right = max(right, y)
        if not placed:
            ans.append([left, right])
        return ans
            
# 138 copy list with random pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    d = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        if head not in self.d:
            headnew = Node(head.val) 
            self.d[head] = headnew
            headnew.next = self.copyRandomList(head.next)
            headnew.random = self.copyRandomList(head.random)
        return self.d[head]
        
        
# better

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        # build
        cur = head
        while head:
            
            headnew = Node(head.val)
            headnew.next = head.next
            head.next = headnew
            head = headnew.next

        curnew = cur 
        while curnew:
            nodenew = curnew.next
            nodenew.random = curnew.random.next if curnew.random != None else None
            curnew = curnew.next.next
        ans = cur.next
        
        '''while node:
            tmp = node.next
            node.next = node.next.next
            node = tmp.next
        return ans
        '''
        while cur:
            noden = cur.next
            cur.next = noden.next
            noden.next = noden.next.next if noden.next != None else None
            cur = cur.next
        return ans

# 61 rotate list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        cur = head
        nums = 0
        while cur:
            nums+= 1
            cur = cur.next
        k %= nums
        cur = head
        for _ in range(k + 1):
            if cur:
                cur = cur.next
        pre = head
        while cur:
            cur = cur.next
            pre = pre.next
        headnew = None
        if pre:
            headnew = pre.next
            pre.next = None
        cur = headnew
        if cur == None:
            return head
        if cur.next == None:
            cur.next = head
            return headnew
        while cur.next:
            cur = cur.next
        cur.next = head
        return headnew

# 48 rotate image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = (n + 1) // 2
        for i in range(n// 2):
            for j in range(m):
                matrix[i][j], matrix[j][n - 1 -i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 -i], matrix[n - 1 - i][n - 1 - j]
        return matrix

# 73

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = False
        col = []
        for i in range(m):
            row = False
            for j in range(n):
                if matrix[i][j] == 0:
                    row = True
                    col.append(j)
            if row:
                for j in range(n):
                    matrix[i][j] = 0
        for j in col:
            for i in range(m):
                matrix[i][j] = 0
        

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int flag_col0 = false, flag_row0 = false;
        for (int i = 0; i < m; i++) {
            if (!matrix[i][0]) {
                flag_col0 = true;
            }
        }
        for (int j = 0; j < n; j++) {
            if (!matrix[0][j]) {
                flag_row0 = true;
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (!matrix[i][j]) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (!matrix[i][0] || !matrix[0][j]) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (flag_col0) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
        if (flag_row0) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
    }
};

# 79 word search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
        def dfs(x, y, cnt, vis):
            if cnt >= len(word) - 1:
                return True
            res = False
            
            for dx, dy in dir:
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n:
                    if vis[x + dx][y + dy]  == False and board[x + dx][y + dy] == word[cnt + 1]:
                        vis[x + dx][y + dy] = True
                        res = res or dfs(x + dx, y + dy, cnt + 1, vis)
                        vis[x + dx][y + dy] = False
            return res
            
     
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis = [[False]*n for _ in range(m)]
                    vis[i][j] = True
                
                    if dfs(i, j, 0, vis):
                        return True
        return False


# 909 snakes and ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def id2rowcol(idx):
            row, col = (idx - 1) // n, (idx-1) % n
            if row % 2 == 1:
                col = n - 1 - col 
            return n - 1 - row, col
        
        vis = set()
        q = [[1, 0]]
        while q:
            cur = q
            q = []
            for idx, step in cur:
                for i in range(1, 7):
                    nxt = idx + i
                    if nxt > n * n:
                        break
                    if nxt == n * n:
                        return step + 1
                    r, c = id2rowcol(nxt)
                    if board[r][c] > 0:
                        nxt = board[r][c]
                    if nxt == n * n:
                        return step + 1
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append([nxt, step + 1])

        return -1



class Solution:
    def snakesAndLadders(self, root: Optional[TreeNode]) -> int:
        q = [root]
        cnt = 1
        ans = 0
        flag = 0
        while q:
            tmp = q
            q = []
            if len(tmp) != cnt or flag == 1:
                flag = 1
                ans += len(tmp)
            for cur in tmp:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            cnt *= 2
        return ans

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
       
        for i in range(32):
            cnt = sum([ (n >> i) & 1 for n in nums])
            if cnt % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans
        
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighb = [[-1, -1], [-1, 0], [-1, 1], [0,-1],[0, 1], [1, -1], [1, 0], [1, 1]]

        m = len(board)
        n = len(board[0])
        for i in range(m):
          for j in range(n):
            cnt = 0
            for dx, dy in neighb:
              if i + dx >= 0 and i + dx < m and j + dy >= 0 and j + dy < n:
                if board[i + dx][j + dy] == 1 or board[i + dx][j + dy] == 3:
                  cnt += 1
            if board[i][j] == 1 and (cnt < 2 or cnt > 3):
              board[i][j] = 3
            if board[i][j] == 0 and cnt == 3:
              board[i][j] = 2
        for i in range(m):
            for j in range(n):
              if board[i][j] == 3:
                board[i][j] = 0
              if board[i][j] == 2:
                board[i][j] = 1
    
# sort colors          
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        right = 0
        while right < n:
            if nums[right] == 0 and nums[left] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            elif nums[left] == 0:
                left += 1
            right += 1 
        
        right = left
        while right < n:
            if nums[right] == 1 and nums[left] != 1:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            elif nums[left] == 1:
                left += 1
            right += 1 
        
# 287 find the duplicate number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #n = len(nums) - 1
        '''ans = 0
        for i, n in enumerate(nums):
            ans ^= i
            ans ^= n
        return ans 
        '''

        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while  slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# move zeros
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for i,x in enumerate(nums):
            if x != 0:
                nums[left] = x
                left += 1
        for i in range(left, n):
            nums[i] = 0
        
# 3 longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        ans = 0
        cnt = Counter()
        for i in range(n):
            cnt[s[i]] += 1
            while cnt[s[i]] > 1:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ans = max(ans, i - left + 1)

        return ans


# 42 trapping rain water

class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0
        for i, x in enumerate(height):
            while st and height[st[-1]] <= x:
                cur = st.pop()
                if not st:
                    continue
                ans += (min(x, height[st[-1]]) - height[cur]) * (i - st[-1] - 1)
            st.append(i)
        return ans