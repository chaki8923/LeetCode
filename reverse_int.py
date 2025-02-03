class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x<0
        
        rs = str(abs(x))[::-1]
        x1 = int(rs)
        if n:
            x1 = -x1

        if x1 < -2**31 or x1 > 2**31 - 1:
            return 0
        else:
            return x1

# テストコード
if __name__ == "__main__":
    x = 123
    solution = Solution()
    res = solution.reverse(nums)
    print("result:", res)
