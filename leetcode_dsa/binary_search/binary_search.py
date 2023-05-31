from typing import List


class MinReturn:

    def findMin(self, nums: List[int]) -> int:
        """i-type: List[int], r-type: [int]
        return the min value of a given integer array.
        """
        l, r = 0, len(nums)-1
        while(l < r):
            mid = int((l+r)/2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid    
        return nums[r]

# Using the special variable 
# __name__
if __name__=="__main__":
    nums = [4, 2, 3]
    solve = MinReturn()
    print(solve.findMin(nums))