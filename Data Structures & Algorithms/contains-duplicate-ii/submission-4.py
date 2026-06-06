class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check_uniq = {}
        for i in range(len(nums)):
            if k == 0:
                return False
            if nums[i] in check_uniq:
                if i - check_uniq[nums[i]] <= k:
                    return True 
            check_uniq[nums[i]] = i
        return False

