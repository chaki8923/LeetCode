class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        count = Counter(nums2)
            
        result = []
        for num in nums1:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
# テストコード
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2,2]
    solution = Solution()
    result = solution.intersect(nums1,nums2)
    print("result", result)