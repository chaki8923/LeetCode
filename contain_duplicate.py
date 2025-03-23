# 重複を削除して配列の中の要素数を返す

class Solution(object):
  def containsDuplicate(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      counter = Counter(nums)
      for i in counter:
          if counter[i] != 1:
              return True
          
      return False

      # 以下のコードの方が早い
      # setは重複を除外して{1,2,3,4}のようになる
      # if len(set(nums))<len(nums):
      #   return True
      # else:
      #   return False

# テストコード
if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4]
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)
