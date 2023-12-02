# -*- coding: utf-8 -*-


class RemoveElement:
    def __init__(self) -> None:
        pass
    
    # q27: Use two pointers, slow and fast
    # slow pointer makes sure all the elements in index [0, slow - 1] is not equal to val
    # fast pointer explores the rest of the array
    def q27_remove_element(self, nums: list[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

    def q844_back_space_compare(self, s: str, t: str) -> bool:
        s_list = [*s]
        t_list = [*t]
        s_len = self.q844_helper_emit_backwards(s_list)
        t_len = self.q844_helper_emit_backwards(t_list)
        if s_len != t_len:
            return False
        else:
            itr_s, itr_t, rlt = len(s_list) - 1, len(t_list) - 1, True
            for i in range(0, s_len):
                if s_list[itr_s] != t_list[itr_t]:
                    rlt = False
                    break
                else:
                    i += 1
                    itr_s -= 1
                    itr_t -= 1

            return rlt

    def q844_helper_emit_backwards(self, chars: list[str]) -> int:
        slow, fast = len(chars) - 1, len(chars) - 1
        count_backwards = 0
        while fast >= 0:
            if chars[fast] == '#':
                count_backwards += 1
                fast -= 1
            elif count_backwards > 0:
                fast -= 1
                count_backwards -= 1
            else:
                chars[slow] = chars[fast]
                slow -= 1
                fast -= 1

        return len(chars) - slow - 1
