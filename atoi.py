class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # 1. Whitespace: Ignore leading whitespace
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            index += 1

        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result *= sign

        # 4. Rounding: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
# テストコード
if __name__ == "__main__":



    s = "1337c0d3"
    solution = Solution()
    res = solution.myAtoi(s)
    print("result:", res)
