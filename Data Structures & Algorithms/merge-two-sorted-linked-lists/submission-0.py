class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Dummy node trick — avoids edge case handling for head
        dummy = ListNode(-1)
        tail = dummy            # tail always points to last node built
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1    # attach smaller node
                list1 = list1.next   # advance that pointer
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next         # move tail forward
        
        # One list exhausted — attach remaining directly (already sorted!)
        tail.next = list1 if list1 else list2
        
        return dummy.next            # skip the dummy node