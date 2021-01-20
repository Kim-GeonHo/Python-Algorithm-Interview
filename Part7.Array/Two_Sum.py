from typing import List

class solution:
    def brute_force(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            for num in nums[index + 1:]:
                if num + nums[index] == target:
                    return [index, nums.index(num)]

        # for i in range(len(nums)):
        #   for j in range(i+1, len(nums)):
        #       if nums[i] + nums[j] == target:
        #           return [i, j]
        return None

    def using_in(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target - nums[i])]

    def hash_map(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            hash_map[n] = i
            if target - n in hash_map:
                return [hash_map[target - n], i]
    
    def two_pointer(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while right - left:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1

            else:
                return [left, right]

sol = solution()

nums = list(map(int, input().split()))
target = int(input())


print(sol.brute_force(nums, target))
print(sol.using_in(nums, target))
print(sol.hash_map(nums, target))
print(sol.two_pointer(nums, target))


