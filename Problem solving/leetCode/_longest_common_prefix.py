"""
Problem leetcode url: https://leetcode.com/problems/longest-common-prefix/
Problem title: 14. Longest Common Prefix
Solution:
"""


class LongestCommonPrefix:
    def solution1(self, strs):
        if not strs:
            return ''
        short = min(strs, key=len)
        for i, c in enumerate(short):
            for s in strs:
                if s[i] != c:
                    return short[:i]
        return short


if __name__ == '__main__':
    obj = LongestCommonPrefix()
    print(obj.solution1(['aabsdasdfs', 'aabsdf', 'aabssfddf']))
