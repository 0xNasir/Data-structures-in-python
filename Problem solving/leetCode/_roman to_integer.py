"""
Problem leetcode url: https://leetcode.com/problems/roman-to-integer/
Problem title: 13. Roman to Integer
Solution:
"""


class RomanToInteger:
    romanToIntDict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def solution1(self, s):
        intval = 0
        for i in range(0, len(s) - 1):
            r = s[i]
            next = s[i + 1]
            if self.romanToIntDict[r] < self.romanToIntDict[next]:
                intval -= self.romanToIntDict[r]
            else:
                intval = intval + self.romanToIntDict[r]
        intval = intval + self.romanToIntDict[s[len(s) - 1]]
        return intval

    def solution2(self, s):
        t = 0
        prev = 0
        for i in s[::-1]:
            if prev > self.romanToIntDict[i]:
                t -= self.romanToIntDict[i]
            else:
                t += self.romanToIntDict[i]
            prev = self.romanToIntDict[i]
        return t


if __name__ == '__main__':
    obj = RomanToInteger()
    print(obj.solution1('XXVII'))
    print(obj.solution2('XXVII'))
