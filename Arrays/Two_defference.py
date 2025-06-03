# Similar to LeetCode-01
class solution:
    def twoDiff(self, nums, target_diff):
        pair_idx = {}
        for i, num in enumerate(nums):
            if (num + target_diff) in pair_idx:
                return [i, pair_idx[num + target_diff]]
            if (num - target_diff) in pair_idx:
                return [i, pair_idx[num - target_diff]]
            pair_idx[num] = i


sol = solution()
result = sol.twoDiff([5,20,3,2,50,80], 78)
print(result)