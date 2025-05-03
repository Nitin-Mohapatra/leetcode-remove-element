class Solution:
    def removeElement(self, nums, val):
        k = 0
        for index, ele in enumerate(nums):
            if ele != val:
                nums[k] = ele
                k += 1
        return k

s1 = Solution()
print(s1.removeElement([3, 2, 2, 3], 3))  # Output: 2
