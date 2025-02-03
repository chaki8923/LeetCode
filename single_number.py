class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result ^= i
        return result

# テストコード
if __name__ == "__main__":
    nums = [1,2,2,3,3]
    solution = Solution()
    result = solution.singleNumber(nums)
    print("single number>>>>>>>:", result)
