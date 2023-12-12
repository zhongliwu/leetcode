# -*- coding: utf-8 -*-


def _844_back_space_compare(s: str, t: str) -> bool:
    s_list = [*s]
    t_list = [*t]
    s_len = emit_backwards(s_list)
    t_len = emit_backwards(t_list)
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


def emit_backwards(chars: list[str]) -> int:
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