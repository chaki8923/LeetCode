class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)

        # 2. 最初に出現回数が1の文字を探す
        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        return -1

# テストコード
if __name__ == "__main__":
    s = "abbaacii"
    solution = Solution()
    res = solution.firstUniqChar(s)
    print("result:", res)
