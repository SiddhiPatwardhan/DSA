
class solution:
    def twoSum(self,nums,target):
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i,pair_idx[target-num]]
            pair_idx[num] = i

sol = solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)