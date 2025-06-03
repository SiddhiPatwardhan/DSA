# We have to return the number of times the value(val) is repeated
class solution:
    def removeElement(self ,nums,val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
sol = solution()
result = sol.removeElement([3,2,2,3] , 3)
print(result)