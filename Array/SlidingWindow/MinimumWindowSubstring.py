"""
Leetcode 76: https://leetcode.cn/problems/minimum-window-substring/description/
"""

def minWindow(s: str, t: str) -> str:
    res = ""
    res_len = float('inf')
    t_dict = {}
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    left = right = 0
    win_dict = {}
    while right < len(s):
        # Expand the window by adding the character at `right`
        win_dict[s[right]] = win_dict.get(s[right], 0) + 1
        right += 1
        # Shrink the window as long as it contains all required characters
        while all(key in win_dict and win_dict[key] >= value for key, value in t_dict.items()):
            if (right - left) < res_len:
                res_len = right - left
                res = s[left:right]
            # Remove the character at `left` and move the window forward
            win_dict[s[left]] -= 1
            if win_dict[s[left]] == 0:
                win_dict.pop(s[left])
            left += 1
    return res

if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))