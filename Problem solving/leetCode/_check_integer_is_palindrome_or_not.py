"""
Problem leetcode url: https://leetcode.com/problems/palindrome-number/
Problem title: 9. Palindrome Number
Solution:
"""


class Palindrome:
    def __init__(self):
        pass

    def isPalindrome(self, n: int) -> bool:
        t: bool = True
        s = str(n)
        last = len(s) - 1
        for i in range(len(s)):
            if s[i] != s[last]:
                t = False
                break
            last -= 1
        return t


if __name__ == '__main__':
    pl = Palindrome()
    print('Is 25652 plaindome: ' + str(pl.isPalindrome(25652)))
    print('Is 645346 plaindome: ' + str(pl.isPalindrome(645346)))
