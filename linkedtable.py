
# 143

class Solution:

    def middleNode(self, head:Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


    def reorderList(self, head:Optional[ListNode]) -> None:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)

        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2
            
# 19

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummpy = ListNode(next=head)
        right = dummpy
        for _ in range(n):
            right = right.next
        left = dummpy
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummpy.next

# 82

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummpy = ListNode(next=head)

        cur = dummpy

        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummpy.next