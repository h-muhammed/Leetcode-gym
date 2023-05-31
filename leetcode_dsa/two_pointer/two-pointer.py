from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """

        """
        l = 0
        r = len(height)-1
        result = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)
            if height[l]>height[r]: r -= 1
            else: l += 1
        return result

#Python solution: 1968-array-with-elements-not-equal-to-average-of-neighbors
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """itype: List[int]
        rtype: List[int]
        checking the average of two adjacent
        numbers of a number is not equal.
        """
        for idx in range(1, len(nums)-1):
            if (nums[idx-1] > nums[idx] > nums[idx+1]):
                nums[idx] = nums[idx] ^ nums[idx+1]
                nums[idx+1] = nums[idx] ^ nums[idx+1]
                nums[idx] = nums[idx] ^ nums[idx+1]
            if (nums[idx-1] < nums[idx] < nums[idx+1]):
                nums[idx] = nums[idx] ^ nums[idx+1]
                nums[idx+1] = nums[idx] ^ nums[idx+1]
                nums[idx] = nums[idx] ^ nums[idx+1]
        return nums
