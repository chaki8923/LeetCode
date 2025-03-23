class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # kがリストの長さより大きい場合の対策
        # nums[-k:]は開始位置が後ろからk番目から最後の要素を取得
        # nums[:-k]は終了位置が後ろからk番目の要素を取得。スタート位置は省略してるので最初からになる
        nums[:] = nums[-k:] + nums[:-k] # num[:]を使用することで元のnumsを更新できる。nums = ...だと別のものになってしまう

# テストコード
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    output = solution.rotate(nums, k)
    print("result>>>>>>>>>", output)
