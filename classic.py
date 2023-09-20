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


