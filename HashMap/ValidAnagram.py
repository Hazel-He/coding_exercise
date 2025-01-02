"""
Leetcode 242: https://leetcode.cn/problems/valid-anagram/description/
"""


def isAnagram1(s: str, t: str) -> bool:
    """
    Method 1 use hash map, it takes more space than method 2
    """
    hashMap = {}
    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1

    for char in t:
        if hashMap.get(char) is None:
            return False
        else:
            hashMap[char] = hashMap.get(char) - 1
            if hashMap[char] == 0:
                hashMap.pop(char)

    if len(hashMap) != 0:
        return False

    return True


def isAnagram2(s: str, t: str) -> bool:
    """
    Method 2 use array, it takes less space than method 1
    ord(char) will return the ASCII value of the character
    ord(char) - ord('a') will return the index of the character in the array
    so "a" will be 0, "b" will be 1, "c" will be 2, and so on
    """
    array = [0] * 26
    for char in s:
        array[ord(char) - ord('a')] += 1

    for char in t:
        array[ord(char) - ord('a')] -= 1

    for num in array:
        if num != 0:
            return False

    return True


if __name__ == "__main__":
    isAnagram1("anagram", "nagaram")
    isAnagram1("rat", "car")
    isAnagram1("a", "ab")
