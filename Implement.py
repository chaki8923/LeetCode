class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_n = len(needle)
        len_h = len(haystack)

        for i in range(len_h-len_n + 1):
            if haystack[i:len_n+i] == needle:
                return i
        return -1
# テストコード
if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    solution = Solution()
    res = solution.strStr(haystack,needle)
    print("result:", res)
