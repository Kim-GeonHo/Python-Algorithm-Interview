from typing import List

class solution:
    def my_self(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for key in range(len(nums) - 2):
            left = key + 1
            right = len(nums) - 1

            while (left != right):
                sum_ = nums[key] + nums[left] + nums[right]

                if sum_ < nums[key] - 1:
                    break

                if sum_ < 0:
                    left += 1

                elif sum_ > 0:
                    right -= 1

                else:
                    result.append([nums[key], nums[left], nums[right]])
                    break

        return result

    def brute_force(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                
                    if nums[i] + nums[j] + nums[k] == 0 :
                        result.append([nums[i], nums[j], nums[k]])

        return result

    def two_pointer(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for key in range(len(nums) - 2):
            left, right = key + 1, len(nums) - 1

            if key > 0 and nums[key] == nums[key - 1]:
                continue
           
            while (left < right):
                sum = nums[key] + nums[left] + nums[right]

                if sum < 0:
                    left += 1

                elif sum > 0:
                    right -= 1

                else:
                    result.append([nums[key], nums[left], nums[right]])
                

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return result

sol = solution()

nums = list(map(int, input().split()))

print(sol.my_self(nums))
print(sol.brute_force(nums))
print(sol.two_pointer(nums))

