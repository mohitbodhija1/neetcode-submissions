class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)       # result list anchor
        curr = dummy              # pointer to build result
        carry = 0

        # Continue while either list has nodes OR carry remains
        while l1 or l2 or carry:

            # Safely get values (treat exhausted list as 0)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10        # 13 // 10 = 1
            digit = total % 10         # 13 % 10  = 3

            curr.next = ListNode(digit)
            curr = curr.next

            # Advance pointers only if not exhausted
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next