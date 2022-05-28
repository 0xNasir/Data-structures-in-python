"""
Problem leetcode url: https://leetcode.com/problems/longest-palindromic-substring/
Problem title: 5. Longest Palindromic Substring
Solution:
"""


def checkPalindrome(s, i, i1):
    while i >= 0 and i1 < len(s) and s[i] == s[i1]:
        i -= 1
        i1 += 1
    return s[i + 1:i1]


class LongestPalindrom:
    def __init__(self):
        pass

    def solution1(self, s: str) -> str:
        substr: any = ''
        for i in range(len(s)):
            odd = checkPalindrome(s, i, i)
            even = checkPalindrome(s, i, i + 1)
            substr = max(odd, even, substr, key=len)

        return substr

    def solution2(self, s: str) -> str:
        substr: any = ''
        for i in range(len(s)):
            j = k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            odd = s[j + 1:k]
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            even = s[j + 1:k]
            substr = max(odd, even, substr, key=len)

        return substr


if __name__ == '__main__':
    lp = LongestPalindrom()
    print(lp.solution1('abcbabfedsdef'))
    print(lp.solution2('abcbabfedsdef'))
