class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find meeting point inside cycle
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]           # 1 step
            fast = nums[nums[fast]]     # 2 steps
            if slow == fast:
                break                   # cycle detected

        # Phase 2: Find entry point of cycle = duplicate
        slow = 0                        # reset slow to start
        # fast stays at meeting point

        while slow != fast:
            slow = nums[slow]           # both move 1 step
            fast = nums[fast]

        return slow                     # duplicate number
