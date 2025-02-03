# 重複を削除して配列の中の要素数を返す

class Solution(object):
  def removeDuplicate(self, nums):
    seen = set()
    index= 0
    for item in nums:
      if item not in seen:
        seen.add(item)
        nums[index] = item
        index += 1

    return index

# テストコード
if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4]
    solution = Solution()
    length = solution.removeDuplicate(nums)
    print("Unique elements count:", length)
    print("Updated list:", nums[:length])
