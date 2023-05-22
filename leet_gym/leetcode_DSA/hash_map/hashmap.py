from typing import List

class Summation:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        itype: List[int], [int]
        rtype: List[int]
        given a set of array integers and a target value\
        return the index of two value which contains the\
        the target value.
        """
        store = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in store:
                return [store.get(complement), idx]
            store[nums[idx]] = idx


class ConNearDuplicate:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """

        """
        hashMap = {}
        for idx in range(len(nums)):
            print(idx)
            if nums[idx] in hashMap and idx-hashMap[nums[idx]]<=k:
                    return True
            else: hashMap[nums[idx]] = idx

        return False
    
class FindIntersect:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        
        """
        result = []
        for idx in range(len(nums1)):
            if nums1[idx] in nums2:
                nums2.remove(nums1[idx])
                result.append(nums1[idx])
        return result
    
class FindDisappears:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """

        """
        check = {}
        result = []
        for ind, item in enumerate(nums):
            check[item] = ind+1
        for ind in range(1, len(nums)+1):
            if ind in check: continue 
            else: result.append(ind)
        return result
    
class CheckDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """itype: List[int], rtype: bool
        return true if any duplicates available
        else return false
        """
        check_duplicate = {}
        for idx in range(len(nums)):
            check_duplicate[nums[idx]] = 0
        for idx in range(len(nums)):
            check_duplicate[nums[idx]] += 1
        values = check_duplicate.values()
        if max(values) > 1:
            return True
        else: return False

# Using the special variable 
# __name__
if __name__=="__main__":
    target = 6
    nums = [3, 2, 4]
    solve = Summation()
    print(solve.twoSum(nums, target))

    target = 6
    nums = [3, 2, 4]
    solve = ConNearDuplicate()
    print(solve.containsNearbyDuplicate(nums, target))

    nums1 = [3, 2, 4]
    nums2 = [2, 4]
    solve = FindIntersect()
    print(solve.intersect(nums1, nums2))

    nums = [4,3,2,7,8,2,3,1]
    solve = FindDisappears()
    print(solve.findDisappearedNumbers(nums))

    nums = [4,3,2,7,8,2,3,1]
    solve = CheckDuplicate()
    print(solve.containsDuplicate(nums))
