class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# テストコード
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    solution = Solution()
    output = solution.longestCommonPrefix(strs)
    print("result>>>>>>>>>", output)
