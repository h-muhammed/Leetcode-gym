class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)):
            match_count = 0
            for c in range(len(needle)):
                # print(f'{needle[c]} {haystack[idx+c]}')
                if needle[c] == haystack[idx+c]:
                    match_count =+ 1
                else:
                    # print(idx)
                    idx = idx+c
                    break
            print(match_count)
            if match_count == len(needle):
                
                return idx
            idx = idx+len(needle)
        return -1
haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))