class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) -1 , -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
            
        return [1] + digits

# テストコード
if __name__ == "__main__":
    digits = [1,2,3]
    solution = Solution()
    length = solution.plusOne(digits)
    print("Thus, the result should be:", length)
