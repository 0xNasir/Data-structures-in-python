"""
Problem leetcode url: https://leetcode.com/problems/number-of-1-bits/
Problem title: 191. Number of 1 Bits
Solution:
"""


class Solution:
    def __init__(self):
        pass

    def hammingWeight(self, n: int) -> int:
        bindata: str = format(n, "b")
        count: int = 0
        for i in bindata:
            if i == '1':
                count += 1
        return count


if __name__ == '__main__':
    sob = Solution()
    print(sob.hammingWeight(n=2456))
