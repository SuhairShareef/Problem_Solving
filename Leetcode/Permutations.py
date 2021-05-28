from typing import List
def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        result = []

        for i in range(len(nums)):
            currentItem = nums [i]
            remain = nums[:i] + nums[i + 1:]

            for perm in self.permute(remain):
                result.append([currentItem] + perm)

        return result