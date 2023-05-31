class Solution:
    def reverseWords(self, s: str) -> str:
        """
        :itype, List[List[int]]
        :rtype, List[List[int]]
        :return, merged list.

        Examples
        --------
        input:
        >>> s = "the sky is blue"
        >>> obj = Solution()
        >>> obj.reverseWords(s)
        output:
        >>> "blue is sky the"
        """
        result = ''
        word = []
        for idx in range(len(s)-1, -1, -1):
            if (s[idx]>='a' and s[idx]<='z') or (s[idx] >='A' and s[idx]<='Z') \
            or (s[idx] >= '0' and s[idx] <= '9'):
                word.append(s[idx])
            elif len(word): 
                print(word)
                word.reverse()
                for char in word:
                    result+=char
                result+=' '
                word = []
        if len(word):
            word.reverse()
            for char in word:
                result+=char
        else: return result[:-1]
        return result