def low_bound(nums:List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] >= target :
            right = mid - 1
        else :
            left = mid + 1
    return left
class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = low_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = low_bound(nums, target + 1) - 1
        return [start, end]