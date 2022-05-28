"""
Problem leetcode url: https://leetcode.com/problems/counting-bits/
Problem title: 338. Counting Bits
Solution:
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(0, n + 1):
            bindata: str = format(i, "b")
            count: int = 0
            for j in bindata:
                if j == '1':
                    count += 1
            l.append(count)
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(10))
