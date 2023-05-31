from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        :i-type: class[TreeNode]
        :r-type: List[int]
        :return
        -------
        store each node inorder style from the tree and return it.

        Examples
        --------
        input:
        >>> nums = [3, 2, 4]
        >>> obj = Solution()
        >>> obj.findPeakElement(nums)
        output:
        >>> 2
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (end+start)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else: start = mid + 1
        return start

if __name__ == '__main__':
    nums = [3, 2, 4]
    solve = Solution()
    print(solve.findPeakElement(nums))
