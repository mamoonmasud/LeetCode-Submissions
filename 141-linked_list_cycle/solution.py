class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head == fast:
                return True
        return False
        