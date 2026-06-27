class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        
        while fast and fast.next:      # fast hits None → no cycle
            slow = slow.next           # 🐢 1 step
            fast = fast.next.next      # 🐇 2 steps
            
            if slow == fast:           # met → cycle exists
                return True
        
        return False                   # fast reached end → no cycle