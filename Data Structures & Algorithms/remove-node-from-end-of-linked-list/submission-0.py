# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            # Dummy node points to head — handles edge cases cleanly
            dummy = ListNode(0)
            dummy.next = head

            slow = dummy
            fast = dummy

            # Step 1: Move fast n+1 steps ahead
            # (n+1 so slow lands BEFORE the target, not ON it)
            for _ in range(n + 1):
                fast = fast.next

            # Step 2: Move both until fast hits None
            while fast:
                slow = slow.next
                fast = fast.next

            # Step 3: slow is now just before the target node
            slow.next = slow.next.next  # skip the target

            return dummy.next