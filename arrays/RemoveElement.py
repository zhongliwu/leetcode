# -*- coding: utf-8 -*-


class RemoveElement:
    def __init__(self) -> None:
        pass
    
    # Use two pointers, slow and fast
    # slow pointer makes sure all the elements in index [0, slow - 1] is not equal to val
    # fast pointer explores the rest of the array
    def q27removeElement(self, nums: list[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow